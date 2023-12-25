


<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

PROJECT IS NOT MAINTAINED. MIGHT BE DEPRECIATED.
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/EmperorShade/delugerpg-autocatcher">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">DelugeRPG Autocatcher</h3>

  <p align="center">
    A bot that automatically catches legendary Pokemon
    <br />
    <a href="https://github.com/EmperorShade/delugerpg-autocatcher"><strong>Project Link »</strong></a>
    <br />
    <br />
    <a href="https://github.com/EmperorShade/delugerpg-autocatcher">View Demo</a>
    ·
    <a href="https://github.com/EmperorShade/delugerpg-autocatcher/issues">Report Bug</a>
  
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
   <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#disclaimer">Disclaimer</a></li>
      <li><a href="#features">Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#customization-optional">Customiztion</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project




DelugeRPG is a 2d Pokemon-based Browser Fangame where you can catch, trade and battle your own pokemon online.

This Autocatcher bot finds and catches legendary Pokemon automatically on DelugeRPG - because you don't have to. Based on Python, this bot is powerful as well as customizable

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Disclaimer

The purpose of this project is based solely on studying concepts and should NOT be used as a way to gain unfair advantages in the game. The [creator](https://github.com/EmperorShade/delugerpg-autocatcher) does not promote such unfair means.


### Features

#### <u>Catches legendary Pokemon
This bot searches for and catches legendary Pokemon with a Masterball. Any other Pokemon which you want can also be specefied (Look at <a href="#readme-top">here</a> to learn more).

[![Product Name Screen Shot][product-screenshot]](https://github.com/EmperorShade/delugerpg-autocatcher/screenshot.jpg)
 
 #### <u>Buys Masterballs when out of stock</u>
 Just  be sure to have enough Pokecoins with you.
 
[![Product Name Screen Shot][pokemart-image]](https://github.com/EmperorShade/delugerpg-autocatcher/pokemart.jpg)
#### <u> Sends Windows notification

Sends a Windows notification which includes the name of the Pokemon and the current legendary streak.
  
[![notification image][notification-image]](https://github.com/EmperorShade/delugerpg-autocatcher/notification.png)

#### <u>Records updates in a logs.txt file
Records and updates a list of logins, masterball purchases and legendary Pokemon found along with a timestamp

[![logs photo][logs-image]](https://github.com/EmperorShade/delugerpg-autocatcher/logs.jpg)

#### <u>Opens a different map at random intervals
This feature makes the bot more realistic and also makes chance for catching a variety of legendary Pokemon.
 
<!-- GETTING STARTED -->
## Getting Started

Follow these steps to get your Auto-catcher up and ready.

### Clone the Repo

In the Terminal, navigate to the folder where you want to clone the repository.
Then type this:
```sh
   git clone https://github.com/EmperorShade/delugerpg-autocatcher
```


### Prerequisites

This program requires a Python version of version 3.9.x or later.<br>
To check if you have Python installed, go to the Terminal and type:

```sh
   python
```
It should return something like this:

[![check python][python-check]](https://github.com/EmperorShade/delugerpg-autocatcher/python_check.png)


This also requites a chromedriver of the same version of your Chrome browser.
To get this,
  * Go to Chrome.
  * Type ``` chrome://version/ ``` and check your version.
  * Now search for https://chromedriver.chromium.org/downloads and download a build of the same version.
  * Place the `` chromedriver.exe `` file in the same location as `` autocatcher.py ``
  
  
### Installation


This program uses the following modules:
* Selenium
* Undetected-Chromedriver
* Winotify

You can install the required pakages automatically by:
  ```sh
  pip install -r requirements.txt
  ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Username and password<br>


Add your username and password in ```credentials.py``` within the double-quotes (" ").
For example:

```sh
id = ("Example_ID")
passwd = ("password")
````

<!-- USAGE EXAMPLES -->
## Usage

To run the program, locate to the location of the repo and simply type:
```sh
   python .\autocatcher.py
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Customization (optional)

### Custom Pokemon

To add Pokemon other than legendary to your search,
* Go to ```.\files_and_assets``` folder.
* Open ```pokemon_list.py``` file.
* Type the name of your Pokemon in the same way as other legendaries (do not forget the comma).

For example, to add Pikachu and Retro Pokemon to the search:

[![customize pokemon][pokemon-list]](https://github.com/EmperorShade/delugerpg-autocatcher/images/pokemonlist.png)

### Maps

To add any map other than the selected few,
* Locate to ```.\files_and_assets```.
* Open ```maps.py```.
* Add the entire map link to the array the same way as other maps.

<i>(No image.. Cmon you can do this on your own)</i>
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [Lisence](https://github.com/EmperorShade/delugerpg-autocatcher/blob/main/LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Discord - [@shadeslayer69#5141](https://discord.com/users/925683618804826133)

Project Link: [https://github.com/EmperorShade/delugerpg-autocatcher](https://github.com/EmperorShade/delugerpg-autocatcher)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[forks-shield]: https://img.shields.io/github/forks/EmperorShade/delugerpg-autocatcher?style=for-the-badge
[forks-url]: https://github.com/EmperorShade/delugerpg-autocatcher/network/members
[stars-shield]:https://img.shields.io/github/stars/EmperorShade/delugerpg-autocatcher?style=for-the-badge
[stars-url]: https://github.com/EmperorShade/delugerpg-autocatcher/stargazers
[issues-shield]:https://img.shields.io/github/issues/EmperorShade/delugerpg-autocatcher?color=yellow&style=for-the-badge
[issues-url]: https://github.com/EmperorShade/delugerpg-autocatcher/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/EmperorShade/delugerpg-autocatcher/blob/master/LICENSE

[product-screenshot]: images/screenshot.jpg
[pokemart-image]: images/pokemart.jpg
[notification-image]: images/notification.png
[logs-image]: images/logs.jpg
[pokemon-list]: images/pokemonlist.png
[python-check]: images/python_check.png
[terminal-data]: iamges/terminal.png
