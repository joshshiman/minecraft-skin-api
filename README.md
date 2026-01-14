# Minecraft Skin API

A simple FastAPI service that retrieves the skin texture URL for a given Minecraft username.

## Features

-   Fetches a Minecraft user's UUID from their username.
-   Retrieves profile properties from Mojang's session server.
-   Decodes the skin data to return the direct URL to the skin texture.

## Prerequisites

-   Python 3.8+
-   pip

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/josho/minecraft-skin-api.git
    cd minecraft-skin-api
    ```

2.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Start the FastAPI server:

    ```bash
    fastapi dev main.py
    ```
    
    Or for production:
    ```bash
    fastapi run main.py
    ```

2.  The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Get Skin URL

Retrieves the skin URL for a specific Minecraft username.

-   **URL:** `/`
-   **Method:** `POST`
-   **Query Parameters:**
    -   `name` (string): The Minecraft username.

#### Example Request

```bash
curl -X POST "http://127.0.0.1:8000/?name=Notch"
```

#### Example Response

The response is a plain string containing the URL to the skin texture.

```json
"http://textures.minecraft.net/texture/292009a4925b58f02c77dadc3ecef07ea4c7472f64e0fdc32ce5522489362680"
```

## specific implementation details

The application performs the following steps:
1.  Queries `https://api.mojang.com/users/profiles/minecraft/{name}` to get the user's UUID.
2.  Queries `https://sessionserver.mojang.com/session/minecraft/profile/{id}` to get the profile data.
3.  Decodes the Base64 encoded `properties` value to find the skin URL.