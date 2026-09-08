
from scraper import get_product_details
from database import create_database, add_product, get_products
from notifier import price_alert


def main():

    create_database()

    print("=" * 40)
    print("       SMART PRICE TRACKER")
    print("=" * 40)

    while True:

        print("\n1. Add Product")
        print("2. View Products")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            url = input("\nEnter product URL: ")

            try:
                name = get_product_details(url)

                print("\nProduct found:")
                print(name)

                target_price = float(
                    input("Enter target price: ₹")
                )

                current_price = float(
                    input("Enter current price: ₹")
                )

                add_product(
                    name,
                    url,
                    target_price,
                    current_price
                )

                price_alert(
                    name,
                    current_price,
                    target_price
                )

                print("\n✅ Product added successfully!")

            except Exception as e:
                print("\n❌ Error:", e)

        elif choice == "2":

            products = get_products()

            if not products:
                print("\nNo products tracked yet.")

            else:
                print("\nTracked Products:")
                print("-" * 50)

                for product in products:
                    print("ID:", product[0])
                    print("Name:", product[1])
                    print("URL:", product[2])
                    print("Target Price: ₹", product[3])
                    print("Current Price: ₹", product[4])
                    print("Last Checked:", product[5])
                    print("-" * 50)

        elif choice == "3":

            print("\nThank you for using Price Tracker!")
            break

        else:
            print("\n❌ Invalid choice!")


if __name__ == "__main__":
    main()
