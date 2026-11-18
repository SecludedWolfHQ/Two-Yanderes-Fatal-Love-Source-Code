# Detect the initial translation from the device language.
# Ren'Py remembers later language choices in the player's preferences.
define config.enable_language_autodetect = True
define config.default_language = None

init python:

    def get_device_translation_language(device_language, device_region):

        language_code = str(device_language or "").strip().lower().replace("-", "_").split("_", 1)[0]

        return {
            "tr": "turkish",
            "es": "spanish",
            "ru": "russian",
        }.get(language_code)

    def synchronize_localized_language():

        persistent.language = {
            "turkish": "Türkçe",
            "spanish": "Español",
            "russian": "Russian",
        }.get(_preferences.language, "English")

    config.locale_to_language_function = get_device_translation_language

    for translation_language in (None, "turkish", "spanish", "russian"):
        config.language_callbacks[translation_language].append(synchronize_localized_language)
