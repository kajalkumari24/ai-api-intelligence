from inference import predict_api_category
test_cases = [
    ("CoinGecko", "Cryptocurrency prices, market cap, and trading volume data"),
    ("OpenWeatherMap", "Current weather and forecast data for any location"),
    ("PetFinder", "Search adoptable pets from shelters and rescues"),
    ("GitHub API", "Access repositories, issues, and pull requests programmatically"),
    ("MalwareBazaar", "Share and analyze malware samples and threat indicators"),
    ("ArtStation", "Browse digital art and portfolios from artists worldwide"),
    ("Twilio", "Send SMS, voice calls, and video communications via API"),
    ("NASA Open API", "Astronomy pictures, Mars rover photos, and space data"),
]

for name, desc in test_cases:
    result = predict_api_category(name, desc)
    print(f"{name:<20} → {result}")