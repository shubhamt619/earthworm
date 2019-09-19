# e@rthw0rm
##### A python package by Shubham Thakur

Hello All !

This is the Second release of my python package.
Basically this is like a boilerplate for creating your own python package.

### Can it tell me my future ?
##### --> Can you ?

### Will it help me invest in the right cryptocurrency ?
##### --> No

### Okay Then, What it does ?
##### --> Basically, Nothing :P ,  You can clone this repo and simply edit it and publish it to either test PyPi or Live PyPi.

### Wait, It does Nothing at all ?
##### --> It can do a few things allright. See the examples below.

#### Note : Make sure you Install and Import this package first.
##### Install Command - `pip install earthworm-shubhamt619`
##### Import like this `import earthworm`
##### Example 1 : Saying Hello
###### To say hello to a person, all you have to do is call `sayHello()` like,
`earthworm.sayHello("Shubham")`
Output is 
`Hello there Shubham !`

##### Example 2 : Saying Hi
###### To say Hi to a person, all you have to do is call `sayHi()` like,
`earthworm.sayHi("Shubham")`
Output is 
`Hi there Shubham !`


##### Example 3 : Saying PipPip
###### To say PipPip to a person, all you have to do is call `sayPipPip()` like,
`earthworm.sayPipPip("Shubham")`
Output is 
`PipPip Shubham !`

## Upload my package
#### Okay, I have made changes to this repo, How to upload it to PyPi ?
-> 1] Make account on [https://test.pypi.org] and [https://pypi.org]

-> 2] Create a file in your $HOME with name `.pypirc` with the following.

>[distutils]
>    index-servers=
>        pypi
>        testpypi
>
>    [pypi]
>    username: <YOUR_USERNAME>
>    password: <YOUR_PASSWORD>
>
>    [testpypi]
>    repository: https://test.pypi.org/legacy/
>    username: <YOUR_USERNAME>
>    password: <YOUR_PASSWORD>

##### 3] Then install required packages - *setuptools* and *wheel* 
`sudo python3 -m pip install --user --upgrade setuptools wheel`
#### For Python 2.*
`sudo python -m pip install --user --upgrade setuptools wheel`

##### 4]  Go to the root directory of your package (Where `setup.py` exists) and run the following command.
>`sudo python3 setup.py sdist bdist_wheel`

This will generate a `dist/` folder for uploading to `test pypi` or `pypi`.

##### 5]  Install twine
>`sudo python3 -m pip install --user --upgrade twine`

Twine helps you upload your packages to `test pypi` and `pypi` very easily.

### Final Step
##### 6]  Upload your package ! ! !
For `test pypi`
>`sudo python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
 
For PyPi
> `sudo python3 -m twine upload dist/*` 

##### Hey, How can i update my package ?
-> The same way you uploaded the package. First Make version change in `setup.py` and increment the version.
> e.g. 0.0.1 -> 0.0.2

After that, repeat step 4 and 6 to generate `dist/` and reupload newer version of your package.