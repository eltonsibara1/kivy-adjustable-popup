# kivy-adjustable-popup
This project demonstrates how to create a customizable popup in Kivy, where the popup adjusts its height based on its content dynamically. Users can manually set the width, while the height adjusts automatically according to the content size. This feature is ideal for scenarios where you want the popup to adapt to varying content lengths.

• Features:

Dynamic Height: The popup automatically adjusts its height to fit the content inside (e.g., text, buttons).
Customizable Width: You can set the width of the popup manually.
ScrollView: Supports scrolling when content exceeds the maximum height, ensuring a smooth user experience.

• Styling: 

Customizable appearance with the ability to change title fonts, colors, and radius for rounded corners.
Installation
To use this code, you'll need to have Kivy installed. If you don't have Kivy installed, you can install it via pip:
> pip install kivy
• Here is a breakdown of how the adjustable popup works:

Adjustable Height: The popup's height automatically adjusts based on its content size. The label text or buttons inside the popup determine the height, and the popup resizes accordingly.
Manual Width Adjustment: The width of the popup can be manually set, but the height is calculated dynamically based on the content.
Scroll Support: If the popup's content exceeds the specified height, the content becomes scrollable using a ScrollView.

Example Code:
The following Python code creates a custom popup in Kivy that adjusts its height automatically based on its content:

py
