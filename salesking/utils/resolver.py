from __future__ import division, unicode_literals

import operator
import sys
import os
import logging
import contextlib
import json

from jsonschema.compat import urljoin, urldefrag
from jsonschema.exceptions import RefResolutionError


PY3 = sys.version_info[0] >= 3

if PY3:

    basestring = unicode = str
    iteritems = operator.methodcaller("items")
else:

    iteritems = operator.methodcaller("iteritems")

from jsonschema import RefResolver

from salesking.exceptions import SalesKingException

log = logging.getLogger(__name__)


class LocalRefResolver(RefResolver):
    def resolve_local(self, uri, base_uri, ref):
        """
        Resolve a local ``uri``.
         Does not check the store first.

         :argument str uri: the URI to resolve
         :returns: the retrieved document

        """
        # read it from the filesystem
        file_path = None
        # make the reference saleskingstyle
        item_name = None
        if (uri.startswith(u"file") or
                uri.startswith(u"File")):
            if ref.startswith(u"./"):
                ref = ref.split(u"./")[-1]
                org_ref = ref
            if ref.find(u"#properties") != -1:
                ref = ref.split(u"#properties")[0]
            if ref.find(u".json") != -1:
                item_name = ref.split(u".json")[0]

        # on windwos systesm this needs to happen
        if base_uri.startswith(u"file://") is True:
            base_uri = base_uri.split(u"file://")[1]
        elif base_uri.startswith(u"File://") is True:
            base_uri = base_uri.split(u"File://")[1]

        file_path = os.path.join(base_uri, ref)
        result = None
        try:
            schema_file = open(file_path, "r").read()
            result = json.loads(schema_file.decode("utf-8"))
        except IOError as e:
            log.error(u"file not found %s" % e)
            msg = "Could not find schema file. %s" % file_path
            raise SalesKingException("SCHEMA_NOT_FOUND", msg)

        if self.cache_remote:
            self.store[uri] = result
        return result


    @contextlib.contextmanager
    def resolving(self, ref):
        """
        Context manager which resolves a JSON ``ref`` and enters the
        resolution scope of this ref.

        :argument str ref: reference to resolve

        """
        # print u"resol_scope: %s, ref: %s" % (self.resolution_scope, ref)
        full_uri = urljoin(self.resolution_scope, ref)
        uri, fragment = urldefrag(full_uri)
        if not uri:
            uri = self.base_uri

        if uri in self.store:
            document = self.store[uri]
        else:
            if (uri.startswith(u"file") or uri.startswith(u"File")):
                try:
                    document = self.resolve_local(full_uri, self.resolution_scope, ref)
                except Exception as exc:
                    raise RefResolutionError(exc)
            else:

                try:
                    document = self.resolve_remote(uri)
                except Exception as exc:
                    raise RefResolutionError(exc)

        old_base_uri, self.base_uri = self.base_uri, uri
        try:
            with self.in_scope(uri):
                yield self.resolve_fragment(document, fragment)
        finally:
            self.base_uri = old_base_uri
