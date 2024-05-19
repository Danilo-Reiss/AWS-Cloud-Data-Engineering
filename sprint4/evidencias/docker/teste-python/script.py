import requests
import numpy as np

def main():
    print("Hello, Docker!")
    response = requests.get("https://api.github.com")
    print("GitHub API Status:", response.status_code)
    array = np.array([1, 2, 3])
    print("Numpy array:", array)

if __name__ == "__main__":
    main()