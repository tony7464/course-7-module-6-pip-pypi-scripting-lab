from lib.generate_log import fetch_data, generate_log

if __name__ == "__main__":
    post = fetch_data()
    title = post.get("title", "No title found")
    print("Fetched Post Title:", title)

    generate_log([
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched post title: {title}",
    ])
