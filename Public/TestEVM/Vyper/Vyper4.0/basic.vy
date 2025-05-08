MAX_GREETING_LENGTH: constant(uint256) = 100

# State variables
greeting: public(String[MAX_GREETING_LENGTH])
owner: public(address)

MAX_HISTORY_SIZE: constant(uint256) = 10

# Static array (fixed-size list)
supported_languages: public(uint256[MAX_HISTORY_SIZE][3])  # Array of 3 language names, each up to 10 chars

# Dynamic array
greeting_history: public(DynArray[String[MAX_GREETING_LENGTH], 10])  # Store up to 10 previous greetings

# Mappings (hashmaps)
language_to_greeting: public(HashMap[address, String[100]])  # Map language code to greeting
user_favorite_language: public(HashMap[address, String[10]])  # Track user's favorite language
