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
      "win_delay_load_hook": "false",
      "sources": [ "src/schema.cc", "src/xml_errors.cc", "src/node_libxml_xsd.cc" ],
      "include_dirs": [
      	"<!(node -e \"require('nan')\")",
      	'<@(xmljs_include_dirs)'
      ],
      "cflags": ["-Wall"],
      "xcode_settings": {"OTHER_CFLAGS": ["-Wall"]},
      'link_settings': {
        'libraries': [
          '<@(xmljs_libraries)'
        ]
      },
      "conditions": [
          [
              'OS=="mac"',
              {
                  # node-gyp 2.x doesn't add this anymore
                  # https://github.com/TooTallNate/node-gyp/pull/612
                  "xcode_settings": {
                      "CLANG_CXX_LANGUAGE_STANDARD": "c++17",
                      "OTHER_LDFLAGS": ["-undefined dynamic_lookup"],
                  },
              },
          ]
      ],
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
