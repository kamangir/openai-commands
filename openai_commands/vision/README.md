# 🛠️ OpenAI Vision API

Implements the [OpenAI vision API](https://platform.openai.com/docs/guides/vision).

> GPT-4 with Vision ... `GPT-4V` or `gpt-4-vision-preview` in the API ... model ... take in images and answer questions about them
> ... not stateful ... ([more](https://arash-kamangir.medium.com/%EF%B8%8F-openai-vision-1-fb3691bd095a))

Example use on the images ingested from the traffic cameras in downtown Vancouver, using [vancouver-watching 🌈](https://github.com/kamangir/vancouver-watching),

```bash
@openai vision \
    "list some of the things that you see in these images." \
    - Davie,Bute,.jpg \
    $(@mlflow tags search area=vancouver,ingest,published \
        --log 0 \
        --count 1 \
        --offset 0) \
    --max_count 10 \
    --verbose 1
```

| ![image](https://github.com/kamangir/assets/blob/main/vanwatch/2023-11-25-openai-vision/ButeNorthDavie.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/vanwatch/2023-11-25-openai-vision/ButeSouthDavie.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/vanwatch/2023-11-25-openai-vision/DavieEastBute.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/vanwatch/2023-11-25-openai-vision/DavieWestBute.jpg?raw=true) |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |

![image](https://github.com/kamangir/assets/blob/main/vanwatch/2023-11-25-openai-vision/marquee.png?raw=true)

> The images show street scenes captured by surveillance cameras at night, and each bears a timestamp and the text "CITY OF VANCOUVER" indicating they're from Vancouver. In the first image, you see a yellow traffic light indicating caution and part of a crosswalk painted in rainbow colors, likely symbolizing support for the LGBTQ+ community. In the second image, there's a view of a city street with pedestrians crossing, some wearing reflective vests, and the storefronts illuminated with bright lights. The third image shows a different angle of a similar street scene with the same vibrant crosswalk and vehicles' headlights creating streaks of light due to the camera exposure. Finally, in the fourth image, there's a view of parked cars and a clearly visible police vehicle, suggesting the presence of law enforcement nearby. The wet pavement suggests it may have rained, and the reflections imply the street is well-lit at night.