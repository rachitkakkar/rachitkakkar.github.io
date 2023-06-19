# My Website
The code and static files for my custom website. The website is custom built using Hugo and TailwindCSS, following a previous version that used Jeykll and the Minimal Mistakes theme.

# Dependencies
- Hugo
- TailwindCSS
- HighlightJS

# How to build locally
- Clone with `git clone`
- Run `npx tailwindcss -i ./static/css/input.css -o ./static/css/index.css --jit --watch` to update the CSS live
- Host a sever with `hugo serve`