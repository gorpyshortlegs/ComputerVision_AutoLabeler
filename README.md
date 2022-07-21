# ComputerVision_AutoLabeler
Automatically labels images for AI model training!
<div id="top"></div>
<!--
*** Thanks for checking out Auto Labeler. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Now go create the AI product of your dreams!
-->

<br />
<div align="center">
  <a href="https://github.com/gorpyshortlegs/ComputerVision_AutoLabeler">
    <img src="Labeller.png" alt="Logo" width="500" height="500">
  </a>

  <h3 align="center">Automatically Label Computer Vision Dataset</h3>

  <p align="center">
    Extremely helpful time saver on certain Computer Vision projects!
    <br />
    <a href="https://github.com/gorpyshortlegs/ComputerVision_AutoLabeler"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://www.youtube.com/channel/UCKPE2Q-d5-WdnDMZ-XlMSDw">View Demo</a>
    ·
    <a href="https://github.com/gorpyshortlegs/ComputerVision_AutoLabeler/issues">Report Bug</a>
    ·
    <a href="https://github.com/gorpyshortlegs/ComputerVision_AutoLabeler/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#example">Example</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



  When creating a computer vision model that requires intra-class classification(Ex. identifying species of a dog) majority of time is spent labelling data. This project aims to make that proccess much faster. All you need is a trained model that can recognize the base object(Ex.recognize a dog). Then using Auto Labeller all you need to do is type in names of different subclasses(Ex. German Sheperd) and using webscraping(or a provided dataset) Auto Labeller will automatically add labelled images to your dataset.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like labelling the same object in each image over and over


Of course, this labeller will only help people using pytorch yolov5 to do intra-class classification. I will be expanding this project to include different model and dataset formats in the future. Thanks to anyone who contributes to this project!


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With
<ol>
<li>Python</li>
<li>PyTorch</li>
<li>Google SerpAPI</li>
</ol>



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Let's get you started!

### Installation


1. Get a free API Key at [https://serpapi.com/users/sign_up](https://serpapi.com/users/sign_up)
2. Clone the repo
   ```sh
   git clone https://github.com/gorpyshortlegs/ComputerVision_AutoLabeler
   ```
3. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
4. Switch best.pt with your base trained model(model that can recognize target object)

5.Run main.py and type in required info
```sh
python3 main.py
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Example
Watch walkthrough video <a href="">here</a>.
Creating a model that can recognize various dog species.
<img src="Dogs.png" alt="Dog" width="500" height="500">

1.Gather images of a few 100 random dogs (Using google <a href="https://serpapi.com">SerpAPI</a>  helps speed up this proccess)

2.Label the dog in each image(Using <a href="https://roboflow.com"> Roboflow </a> or any labelling tool)

<img src="Roboflow.png" alt="Roboflow" width="500" height="500">

3.Use pytorch to train model(<a href="https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data">Pytorch Github Tutorial</a>)

4. Get a free API Key at [https://serpapi.com/users/sign_up](https://serpapi.com/users/sign_up)

5. Clone the repo
   ```sh
   git clone https://github.com/gorpyshortlegs/ComputerVision_AutoLabeler
   ```
6. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
7. Switch best.pt with your trained model weights

8.Run main.py and type in required info
```sh
python3 main.py
```
9.Start entering dog species and watch your dataset grow!

10.Upload dataset to labelling program(like  <a href="https://roboflow.com"> Roboflow </a>) and tweak labels

11.Train model on new dataset!

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes 
4. Push to the Branch 
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Arhant - arhant7c@gmail.com

Project Link: [https://github.com/gorpyshortlegs/ComputerVision_AutoLabeler](https://github.com/gorpyshortlegs/ComputerVision_AutoLabeler)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments



* [Github readme template](https://github.com/othneildrew/Best-README-Template)
* [Roboflow Labelling Tool](https://roboflow.com)


<p align="right">(<a href="#top">back to top</a>)</p>

