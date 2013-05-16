from fanstatic import Library, Resource
import js.jquery

library = Library('blocksit', 'resources')

blocksit = Resource(library, 'blocksit.js',
                    minified='blocksit.min.js',
                    depends=[js.jquery.jquery])
