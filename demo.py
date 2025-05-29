""" Get current market prices from public APIs for comparison """
import asyncio
import aiohttp

async def get_market_prices():
    """Get current prices for user-specified coins from public APIs in a loop until Ctrl+C"""
    print("Fetching Current Market Prices... (Nhấn Ctrl+C để dừng)")

    # Function to create dynamic API URL for CoinGecko
    def get_coingecko_url(symbols):
        formatted_symbols = ",".join(symbols)
        return f"https://api.coingecko.com/api/v3/simple/price?ids={formatted_symbols}&vs_currencies=usd"

    async with aiohttp.ClientSession() as session:
        try:
            while True:
                # User input for coin symbols
                user_input = input("Nhập các ký hiệu coin, cách nhau bởi dấu phẩy (ví dụ: bitcoin,ethereum): ")
                user_symbols = [symbol.strip().lower() for symbol in user_input.split(",")]

                # API configuration
                apis = [
                    {
                        'name': 'CoinGecko',
                        'url': get_coingecko_url(user_symbols),
                        'parser': lambda data: {symbol.upper(): data[symbol]['usd'] for symbol in user_symbols if symbol in data}
                    }
                ]

                for api in apis:
                    try:
                        print(f"Checking {api['name']}...")
                        async with session.get(api['url']) as response:
                            if response.status == 200:
                                data = await response.json()
                                prices = api['parser'](data)
                                for symbol, price in prices.items():
                                    print(f"{symbol}: ${price:,.2f}")
                            else:
                                print(f"HTTP {response.status} error")
                    except Exception as e:
                        print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nĐã dừng chương trình.")

# Run the async function
if __name__ == "__main__":
    asyncio.run(get_market_prices())