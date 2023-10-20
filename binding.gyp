{
  'variables': {
    'xmljs_include_dirs%': [],
    'xmljs_libraries%': [],
  },
  "targets": [
    {
      "target_name": "node-libxml-xsd",
      "product_extension": "node",
      "type": "shared_library",
      "sources": [ "src/schema.cc", "src/xml_errors.cc", "src/node_libxml_xsd.cc" ],
      "include_dirs": [
      	"<!(node -e \"require('nan')\")",
      	'<@(xmljs_include_dirs)'
      ],
      'link_settings': {
        'libraries': [
          '<@(xmljs_libraries)'
        ]
      },
      'default_configuration': 'Release',
      'configurations': {
        'Debug': {
          'defines': [ 'DEBUG', '_DEBUG' ],
          'msvs_settings': {
            'VCCLCompilerTool': {
              'RuntimeLibrary': 1 # static debug
            }
          }
        },
        'Release': {
          'defines': [ 'NDEBUG' ],
          'msvs_settings': {
            'VCCLCompilerTool': {
              'RuntimeLibrary': 0 # static release
            }
          }
        }
      }
    }
  ]
}
