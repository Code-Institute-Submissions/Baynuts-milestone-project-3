# README - Recipe Database Driven Website - Third Milestone

## Table of Contents

- [Description](#Description)
- [UX](#UX)
- [Wireframe](#Wireframe)
- [Screenshots](#Screenshots)
- [Features](#Features)
- [Technologies](#Technologies)
- [Tools](#Tools)
- [Deployment](#Deployment)
- [Testing](#Testing)
- [Credits](#Credits)

## Description

Recipe website where users can view recipes from around the world, once user has signed up they have the option to add their own recipes and edit or delete their own or other users recipes. Recipes are easily viewable on one page but have their own individual pages with the ingredients and method of creation. This project has been writen in Python using the AWS Cloud 9 IDE, Flask has been used to implement the Database that has been created using MongoDB. I have tried to create a modern website which can be easily used by all different types of users. It has a very uncluttered design with navigation at the top where users would expect to find it. The User account buttons have also been placed at the top right as is usually the case. The main recipe list page has the images prominent as I belive that most users would use this as their main form of navigation.

## UX

It has been designed to be current, easy to follow and responsive for mobile and tablet devices. 

- Very user friendly design with standard layout to ease use.
- The view recipes page has been turned in to a grid which all lines up to create a pleasing page which is easily viewable.
- All forms have been created to be easily filled in. Icons have been used on all fields to quickly show the type of field.
- Form fields have helper text to give greater detail to the user what is expected and the length on some fields.
- All forms have the same styling and submit button to ease transition.
- Fully responsive design across the whole site with specific mobile navigation and differing view of the recipes page.
- I did not want just anybody to be able to edit or delete the recipes so I added the sign up feature to limit malicious behaviour.
- Only users that are logged in can view the add recipe link in the navigation and also the edit / delete buttons in the design.
- The use of a modal was a secondary feature that was added due to the ease of deleting a recipe by accident. The modal pops up with a second warning asking to confirm delete.
 
## Wireframe
https://raw.githubusercontent.com/Baynuts/milestone-project-3/master/static/images/wireframe.jpg

## Screenshots

#### Home Page
https://raw.githubusercontent.com/Baynuts/milestone-project-3/master/static/images/screenshot-home.jpg
#### Recipe List Page
https://raw.githubusercontent.com/Baynuts/milestone-project-3/master/static/images/screenshot-recipes.jpg
      
## Features

#### Low load time
All background images have been compressed to speed up site
#### Responsive design
Materialize has been incorporated in to the design as the framework. This gives responsive features out of the box which have then been customised to fit with the design that I envisaged.
#### User Authentication
A signup function has been created, the details of which are sent and saved by the database in a hash sequence which is unreadable by admins.
#### User Level Features
Users are only able to add recipes or edit and delete recipes once they have signed up and logged in. At present the site automaticaly gives new users an account as it is a test site, but it would be easily convertable to allow more security regarding authorising accounts.
#### Parrallax
The home page features a parralax background image which scrolls with the user for increased aesthetics.
#### Social Icons
Prominent social icons in footer which have been colour coded to carry on the colour scheme.
#### Sign Up Page
Gives users the option to sign-up and get access to amend or create recipes.
#### Individual Recipes Pages
Similar to a product page each recipe has its own page with the rating, prep / cooking times, nationality, serving suggestions, ingredients and method of creation.
#### Add Recipe Form
Form created so that registered users can add recipes straight to the database which are then displayed on the site.
#### Edit Recipe Form
Recipe data is pulled from the database and entered in to the form to ease the editting of any recipes.
#### Delete Recipe Modal
When user opts to delete recipe modal pop up appears to ask for confirmation before removing the entry from the database.

### Features to add in future
#### User Home Page
When user logs they would have their own home page with all their own recipes, this would also add the functionality that users can only edit and delete recipes that they had addded.
#### Image store
At present images are inserted in to the design using hyperlinks to hosted images. In future I would prefer to hold the images in a store, it would also give me greater control of the sizes of the images so that the design cannot be broken by different aspect ratios.

## Technologies

#### HTML5
The basic layout of the page has been created using HTML, I have tried to make it as simple as possible and use as little code as possible. This is showing best practice and also helps to make the page load faster.
#### CSS
The HTML has been styled using a separate CSS file. 
#### JavaScript / JQuery
Materialize modules have been initialized and used to aid in the design and functionality of the site.
#### Materialize
Material design framework has been used instead of Bootstrap due to its lightweight framework. Additional features that Bootstrap comes with were not needed so I felt that the lightness of the overall site was more important.
#### Python3
Used to create the main structure of the backend
#### Flask
Imported to handle the website part of the backend
#### WT Forms
Instrumental in the creation of the sign up and login pages
#### Werkzeug Security
Added to increase the security of users details to and from the database and also in the database
#### Jinja
Jinja variable have been used to place the data in to the various templates of the website.
#### MongoDB
Used to hold the NonSQL database that is driving the website
#### GitHub
Code base repository for implemental changes and storage
#### Heroku
The web app has been deployed to Heroku as the host, all secret keys and passwords have been hidden using the config settings available.


## Tools
* VS Code
* AWS Cloud 9
* Google Chrome Developer Tools
* Git
* Github
* Materialize
* W3C Validator
* Adobe Fireworks


## Deployment

The code can be viewed using Heroku: http://online-cookbook-db.herokuapp.com/index

Throughout the development of my project, my development has been committed and pushed to both Github and Heroku. This meant that my work was protected from any hardware issues and also halfway through development AWS Cloud9 did lock access to my account for the weekend, having the repository meant that I could carry on working without access to Cloud9 (VS Code was used while access was denied).
To use Heroku some additional steps need to be taken. A requirements.txt file needs to be created with details of the modules that are needed to run the app, also the Heroku account settings need to be set up with the private details that are not acceptable in the python file, this consist of IP, ROOT, SECRET_KET and MONGO_URI.

## Testing

#### Testing has completed using: 

* W3C validator for both HTML and CSS
* Google Chrome Developer
Chrome developer tools did find some errors in respect to the jQuery additions to Materialize, this related to the mobile responsive side menu, after some fault finding I managed to solve the problem and them amended the code in Cloud9 to resolve the error. When retested the site was error clear.

#### Responsiveness

The site has been tested using iPhone 6, iPhone 8, iPhone 5, Samsung Galaxy Tab, Samsung Galaxy Ace, iPad mini and various laptops and desktops.
On certain devices the text on the recipe list page did overlap each other, this has been amended using media queries for specific sizes so that there is a better use of white space, this ensured that the text was properly spaced and also did not clutter the view.

#### Browsers
I have tested the site using the following browsers

* Google Chrome
* Apple Safari
* Opera
* Internet Explorer
* Mozilla Firefox

I did not find any problems while testing with the differing browsers so no changes were needed to the app.

#### Login Form Testing
The login page / form has been tested with several variations from short usernames to long usernames, the use of special characters did not alter the functionality of the form, this can be used as a specific username or an email address due to the length given for the field.

#### Sign Up Form Testing
The sign up page has been tested using all of the various tests I used for the login page. As before no problems were detected after the form had been set up and amended initially. The only issue that I have with the form as with the other forms is the entering of fields, it seems to be a Materialize issue but you have to click on the line below the field to get the cursor in the box. I have researched the issue and this does appear to be a Materialize problem, I will bear this in mind before choosing materialize for any other projects.

#### Add Recipe Form Testing
The add recipe page was used to add the majority of the recipes on to the site so this has been tested and amended during the development process, I did have issues with some of the fields not drawing the data from the Mongo database but this has now all been cured and performed flawlessly throughout the addition of all the recipes once completed.

#### Edit Recipe Form Testing
While entering the recipes on the site some errors were made when keying the recipes in so the edit recipe form has been used during development to correct spelling errors. As with the add recipe form pulling data from the database did have its issues to be begin with but is now functioning well. One small note is that underscores rather than hyphens should be used when naming fields, using hyphens did cause some problematic errors before I made the connection and corrected the entire set up.

#### Final Testing
I also enlisted friends and family to test all the areas of the site. I few problems have been fixed due to different user testing, one was that they felt the colours of the 'Edit' and 'Delete' buttons should be different, this has now been amended. Also how the images appeared on different devices, this has now been improved so that the view is consistant on different devices, this could be improved by storing the images in the app and being able to crop them or insist on certain aspect ratios.

## Credits

*	I received advice from my mentor, Maranatha Ilesanmi

------------------------------------------------------------