from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import json

# Define the function that creates the UI elements
def create_ui():
    # Create the main window
    window = tk.Tk()
    window.title("Web Scraper")

    # Set the default font for the app
    window.option_add("*Font", "Roboto 12")

    # Set the background color of the app
    window.config(bg="#F7FDFC")

    # Configure the rows and columns of the grid
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=0)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=0)

    # Create a label for the URL
    url_label = tk.Label(window, text="Enter the URL:")
    url_label.grid(row=0, column=0, sticky="w")

    # Create a text field for the URL
    url_entry = tk.Entry(window, borderwidth=0, relief="solid", bg="#FAD5BB")
    url_entry.grid(row=0, column=1, sticky="ew")

    # Create a label for the data to extract
    data_label = tk.Label(window, text="Enter the data you want to extract:")
    data_label.grid(row=1, column=0, sticky="w")

    # Create a text field for the data to extract
    data_entry = tk.Entry(window, borderwidth=0, relief="solid", bg="#FAD5BB")
    data_entry.grid(row=1, column=1, sticky="ew")

    # Define the clear_data() function
    def clear_data():
        # Clear the JSON data
        json_text.delete(1.0, tk.END)

    # Create a button to start the scraping
    scrape_button = tk.Button(window, text="Scrape", command=lambda: scrape_data(url_entry.get(), data_entry.get()), borderwidth=0, relief="solid", bg="#fafafa", activebackground="#fafafa", activeforeground="white")
    scrape_button.grid(row=2, column=1, sticky="ew")

    # Create a Text widget to display the JSON data
    json_text = tk.Text(window, borderwidth=0, relief="solid")
    json_text.grid(row=3, column=0, columnspan=2, sticky="ew")

    # Create a button to clear the JSON data
    clear_button = tk.Button(window, text="Clear", command=clear_data, borderwidth=0, relief="solid", bg="#D4FFF7", activebackground="#C6FDF3", activeforeground="white")
    clear_button.grid(row=4, column=0, columnspan=2, sticky="ew")

    return window