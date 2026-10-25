from typing import Optional

from . import models

PRESETS = {
    "EBC0462E-1FD4-25CD-A21E-A68A0E5DDB23": {
        "siteurl": "https://tinder-api.arkoselabs.com",
        "sitekey": "EBC0462E-1FD4-25CD-A21E-A68A0E5DDB23",
        "apiurl": "https://tinder-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": ["null"],
            "client_config__sitedata_location_href": "about:blank",
            "window__tree_structure": "[[]]",
            "window__tree_index": [0],
        }
    },
    "284CE8B2-89E0-45B0-98B7-38594A810745": {
        "siteurl": "https://customers.payzilch.com",
        "sitekey": "284CE8B2-89E0-45B0-98B7-38594A810745",
        "apiurl": "https://client-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": ["https://customers.payzilch.com"],
            "client_config__sitedata_location_href": "https://customers.payzilch.com/apply/",
            "window__tree_structure": "[[],[],[],[]]",
            "window__tree_index": [3],
        }
    },
    "D5264E07-85CF-434C-88E5-6F095A832C01": {
        "siteurl": "https://customers.payzilch.com",
        "sitekey": "D5264E07-85CF-434C-88E5-6F095A832C01",
        "apiurl": "https://client-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": ["https://customers.payzilch.com"],
            "client_config__sitedata_location_href": "https://customers.payzilch.com/apply/",
            "window__tree_structure": "[[],[]]",
            "window__tree_index": [1],
        }
    },
    "B5B07C8C-F93F-44A8-A353-4A47B8AD5238": {
        "siteurl": "https://tinder-api.arkoselabs.com",
        "sitekey": "B5B07C8C-F93F-44A8-A353-4A47B8AD5238",
        "apiurl": "https://tinder-api.arkoselabs.com",
        
        "data": {
            "window__ancestor_origins": ["https://tinder-api.arkoselabs.com"],
            "client_config__sitedata_location_href": "https://tinder-api.arkoselabs.com/v2/2.12.0/enforcement.0a3d1c68c34cf87e8eedcc692165053d.html",
            "window__tree_structure": "[[]]",
            "window__tree_index": [0],
        }
    },
    "272AEF57-0D14-458A-BCCB-0C2D6CD6494F": {
        "siteurl": "https://signup.microsoft.com/get-started/signup",
        "sitekey": "272AEF57-0D14-458A-BCCB-0C2D6CD6494F",
        "apiurl": "https://microsoft-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": [
                "https://signup.microsoft.com"
            ],
            "client_config__sitedata_location_href": "https://signup.microsoft.com/get-started/signup",
            "window__tree_structure": "[[],[]]",
            "window__tree_index": [1],
        }
    },
    "2CB16598-CB82-4CF7-B332-5990DB66F3AB": {
        "siteurl": "https://iframe.arkoselabs.com/",
        "sitekey": "2CB16598-CB82-4CF7-B332-5990DB66F3AB",
        "apiurl": "https://client-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": [
                "https://iframe.arkoselabs.com",
                "https://x.com",
            ],
            "client_config__sitedata_location_href": "https://iframe.arkoselabs.com/2CB16598-CB82-4CF7-B332-5990DB66F3AB/index.html",
            "window__tree_structure": "[[[]]]",
            "window__tree_index": [0, 0],
        },
    },
    "B7D8911C-5CC8-A9A3-35B0-554ACEE604DA": {
        "siteurl": "https://iframe.arkoselabs.com",
        "sitekey": "B7D8911C-5CC8-A9A3-35B0-554ACEE604DA",
        "apiurl": "https://client-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": [
                "https://iframe.arkoselabs.com",
                "https://signup.live.com",
            ],
            "client_config__sitedata_location_href": "https://iframe.arkoselabs.com/B7D8911C-5CC8-A9A3-35B0-554ACEE604DA/index.html",
            "window__tree_structure": "[[[]],[],[[]]]",
            "window__tree_index": [2, 0],
        },
    },
    "DF9C4D87-CB7B-4062-9FEB-BADB6ADA61E6": {
        "siteurl": "https://demo.arkoselabs.com/",
        "sitekey": "DF9C4D87-CB7B-4062-9FEB-BADB6ADA61E6",
        "apiurl": "https://client-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": [],
            "client_config__sitedata_location_href": "https://demo.arkoselabs.com/",
            "window__tree_structure": "[]",
            "window__tree_index": [],
        },
    },
    "9E881D9A-F495-4A23-BE4B-16067FF8CC3B": {
        "siteurl": "https://iframe.arkoselabs.com",
        "sitekey": "9E881D9A-F495-4A23-BE4B-16067FF8CC3B",
        "apiurl": "https://client-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": [
                "https://iframe.arkoselabs.com",
                "https://www.linkedin.com",
                "https://www.linkedin.com",
                "https://www.linkedin.com",
            ],
            "client_config__sitedata_location_href": "https://iframe.arkoselabs.com/9E881D9A-F495-4A23-BE4B-16067FF8CC3B/index.html",
            "window__tree_structure": "[[],[[[[]]]]]",
            "window__tree_index": [1, 0, 0, 0],
        },
    },
    "85800716-F435-4981-864C-8B90602D10F7": {
        "siteurl": "https://match.com",
        "sitekey": "85800716-F435-4981-864C-8B90602D10F7",
        "apiurl": "https://client-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": ["https://match.com"],
            "client_config__sitedata_location_href": "https://match.com/login",
            "window__tree_structure": "[[]]",
            "window__tree_index": [0],
        },
    },
    "867D55F2-24FD-4C56-AB6D-589EDAF5E7C5": {
        "siteurl": "https://iframe.arkoselabs.com",
        "sitekey": "867D55F2-24FD-4C56-AB6D-589EDAF5E7C5",
        "apiurl": "https://client-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": [
                "https://iframe.arkoselabs.com",
                "https://twitter.com",
            ],
            "client_config__sitedata_location_href": "https://iframe.arkoselabs.com/867D55F2-24FD-4C56-AB6D-589EDAF5E7C5/index.html",
            "window__tree_structure": "[[[]]]",
            "window__tree_index": [0, 0],
        },
    },
    "0152B4EB-D2DC-460A-89A1-629838B529C9": {
        "siteurl": "https://iframe.arkoselabs.com",
        "sitekey": "0152B4EB-D2DC-460A-89A1-629838B529C9",
        "apiurl": "https://client-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": [
                "https://iframe.arkoselabs.com",
                "https://x.com",
            ],
            "client_config__sitedata_location_href": "https://iframe.arkoselabs.com/0152B4EB-D2DC-460A-89A1-629838B529C9/index.html",
            "window__tree_structure": "[[[]]]",
            "window__tree_index": [0, 0],
        },
    },
    "A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F": {
        "siteurl": "https://www.roblox.com",
        "sitekey": "A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F",
        "apiurl": "https://arkoselabs.roblox.com",
        "data": {
            "window__ancestor_origins": [
                "https://www.roblox.com",
                "https://www.roblox.com",
            ],
            "client_config__sitedata_location_href": "https://www.roblox.com/arkose/iframe",
            "window__tree_structure": "[[[]]]",
            "window__tree_index": [0, 0],
        },
    },
    "476068BF-9607-4799-B53D-966BE98E2B81": {
        "siteurl": "https://www.roblox.com",
        "sitekey": "476068BF-9607-4799-B53D-966BE98E2B81",
        "apiurl": "https://arkoselabs.roblox.com",
        "data": {
            "window__ancestor_origins": [
                "https://www.roblox.com",
                "https://www.roblox.com",
            ],
            "client_config__sitedata_location_href": "https://www.roblox.com/arkose/iframe",
            "window__tree_structure": "[[],[[]]]",
            "window__tree_index": [1, 0],
        },
    },
    "747B83EC-2CA3-43AD-A7DF-701F286FBABA": {
        "siteurl": "https://octocaptcha.com",
        "sitekey": "747B83EC-2CA3-43AD-A7DF-701F286FBABA",
        "apiurl": "https://github-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": [
                "https://octocaptcha.com",
                "https://github.com",
            ],
            "client_config__sitedata_location_href": "https://octocaptcha.com/",
            "window__tree_structure": "[[]]",
            "window__tree_index": [0],
        },
    },
    "EA4B65CB-594A-438E-B4B5-D0DBA28C9334": {
        "siteurl": "https://iframe.arkoselabs.com",
        "sitekey": "EA4B65CB-594A-438E-B4B5-D0DBA28C9334",
        "apiurl": "https://snap-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": [
                "https://iframe.arkoselabs.com",
                "https://accounts.snapchat.com",
            ],
            "client_config__sitedata_location_href": "https://iframe.arkoselabs.com/EA4B65CB-594A-438E-B4B5-D0DBA28C9334/lightbox.html",
            "window__tree_structure": "[[[]]]",
            "window__tree_index": [0, 0],
        },
    },
    "CC3F2AEA-6C11-493B-A83B-7BA702D7525F": {
        "siteurl": "https://bumble-api.arkoselabs.com",
        "sitekey": "CC3F2AEA-6C11-493B-A83B-7BA702D7525F",
        "apiurl": "https://bumble-api.arkoselabs.com",
        "data": {
            "window__ancestor_origins": ["https://bumble-api.arkoselabs.com"],
            "client_config__sitedata_location_href": "https://bumble-api.arkoselabs.com/v2/2.11.5/enforcement.54d0c1f02c6eacbecf0b6c6c417771b0.html",
            "window__tree_structure": "[[]]",
            "window__tree_index": [0],
        }
    }
}


def get_preset(sitekey: str) -> Optional[models.Preset]:
    if sitekey not in PRESETS:
        return None
    return models.Preset.from_raw_data(PRESETS[sitekey])