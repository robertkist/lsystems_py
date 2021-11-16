# L-Systems Exploration

A simple L-System generator written in pure Python, with a PySide2 / Qt GUI front-end. This project started out as a 
side-exploration into space filling curves and plant/tree generation.

Run ```src/main_gui.py```. There is no need to run the Makefile, except for running the tests and rebuilding the GUI (Unix-likes only).

### Screenshot
![Main Program Window](https://user-images.githubusercontent.com/9162068/141993730-7752ca51-241e-4380-b9fa-47289bedfbc6.png)

## L-Systems

You can find the axioms, rules and angles for each l-system in the ```src/data/lsystems.json``` file.
Some of the featured l-systems may be unstable - their shapes maybe inverted or other irregularities will
appear between odd and even iteration depths.

### Space filling curves

<table>
    <tr>
        <td><b>Hilbert curve</b></td>
        <td><b>Hilbert curve variation</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956577-778a9b8d-d004-45b0-9a4a-82713f88e87c.png"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956600-fddfe852-03f5-4bc5-b871-e9f9d3769499.png"></td>
    </tr>
</table>

<table>
    <tr>
        <td><b>Peano curve</b></td>
        <td><b>FASS curve 1</b></td>
        <td><b>FASS spiral</b></td>
        <td><b>Quadratic Gosper curve</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956783-c680a72f-4736-4bb7-99d8-8325a30123a9.png"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956427-e169e908-a8e1-4bad-b3cf-f5eefe0ee53d.png"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956461-81562aea-cd39-4c52-8ffd-bfad426ab9c4.png"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956932-b3a08971-62ac-4c69-9932-0fdf11cc3813.png"></td>
    </tr>
</table>

<table>
    <tr>
        <td><b>FASS curve 0</b></td>
        <td><b>FASS curve 2</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956405-8ec432af-9572-4ace-bd57-7aecc3095b02.png"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956441-8531fa43-85b3-40ae-872f-e91482464579.png"></td>
    </tr>
</table>

### Trees

Most tree l-systems are from Lindenmayer, A. and Prusinkiewicz, P. (1990) *The Algorithmic Beauty of Plants*.

<table>
    <tr>
        <td><b>Houdini Tree</b></td>
        <td><b>Tree X</b></td>
        <td><b>Tree B</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956615-df4a1fcf-f87b-447c-8fc9-302c20dfbc29.png" height="260"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957079-19adcec3-01fe-4e65-bccb-2d539ce23bd8.png" height="260"></td>        
        <td><img src="https://user-images.githubusercontent.com/9162068/141957036-d5c3d702-6065-46ab-b355-02d83832b775.png" height="260"></td>
    </tr>
    <tr>
        <td><b>Tree C</b></td>
        <td><b>Tree D</b></td>
        <td><b>Tree E</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957041-b82c456b-a654-4cd4-9397-12bc2b24a5f1.png" height="260"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957048-b86f809f-820e-4396-9f71-9570accf23a5.png" height="260"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957064-b07c41e9-069a-4a87-89f5-e7f90ee9d500.png" height="260"></td>
    </tr>
    <tr>    
        <td><b>Tree Y</b></td>
        <td><b>Tree F</b></td>
        <td><b>Tree A</b></td>    
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957092-44c6b01e-ade1-4bf3-9fb8-06f36714fd12.png" height="260"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957073-8c8d42fe-f03f-4602-9856-e04996679013.png" height="260"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957028-dd5e8e4c-a856-4dad-b81b-de2493d45951.png" height="260"></td>
    </tr>   
</table>

### Circular Shapes & Snowflakes

Note: the Gosper's curve is also a space filling curve.

<table>
    <tr>
        <td><b>Koch Snowflake</b></td>
        <td><b>Snowflake 1</b></td>
        <td><b>Snowflake 2</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956693-81101ea6-9911-4f7d-beea-2fe41e8e497d.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957008-23458fc6-a2b8-4e0e-935c-b4c05ba90a53.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957019-d04501ed-cf3f-4bba-9f74-f316e2ad772f.png" height="200"></td>
    </tr>
    <tr>
        <td><b>Bourke Pentaplexy</b></td>
        <td><b>McWorter Pentigree</b></td>
        <td><b>Gary Teachout Hex-7-b</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956337-a5d6170d-a77f-48f9-bb0d-2fefed1170ba.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956745-8563d084-a805-4003-99d6-85e46ee59777.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956482-7a5e7fff-f750-469f-a2e3-4dff7f1ce56e.png" height="200"></td>
    </tr>
    <tr>
        <td><b>McWorter Penta Snowflake 1</b></td>
        <td><b>McWorter Penta Snowflake 2</b></td>
        <td><b>Anthony Hanmer ADH231a</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957231-24635495-634e-43a9-8fb0-d4fc5e53375f.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957190-8cca5316-e45c-49e8-a526-cd82d10cf263.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956231-009c763d-5288-4b9a-8608-ba2d79f225a6.png" height="200"></td>
    </tr>
    <tr>
        <td><b>Mariano Doily Circle</b></td>
        <td><b>Gosper's curve</b></td>
        <td><b>Levy curve</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956733-ca33ccff-a2ee-4f3b-b446-55f4664a9229.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956501-07230887-1433-4cb7-b2d6-f36d245e1af7.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956713-e9a72b2e-9433-439e-b870-30a3291a5124.png" height="200"></td>
    </tr>
</table>

### Rectangular Shapes

<table>
    <tr>
        <td><b>Fake Peano</b></td>
        <td><b>Serpinski Curve 1</b></td>
        <td><b>Box Fractal</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956797-cf971ffe-abf5-49a6-aa13-62737dfcd514.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956982-716a2cef-aabd-4010-9d51-e1f149e2b551.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956374-bf829b24-7fc7-49dc-bbae-0d396d93275d.png" height="200"></td>
    </tr>
    <tr>
        <td><b>McWorter Serpinski Box (unstable)</b></td>
        <td><b>Serpinski Curve 2</b></td>
        <td><b>Box Crystal</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141983977-0f27ef20-8bbc-4dd9-b2ac-85be3a88c8d6.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957241-29076859-e65c-4f43-8167-7fe00792e963.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956353-bc124eda-5846-426d-a2c1-d566dfcc222a.png" height="200"></td>
    </tr>
    <tr>
        <td><b>Ice Fractals</b></td>
        <td><b>Serpinski Carpet</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956629-25f0d0c6-7f07-491a-903a-1d6d7af28293.png" height="200"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956970-f7655c2e-4a29-4cde-9904-7aded35c10e0.png" height="200"></td>
    </tr>
</table>

### Triangle Shapes

<table>
    <tr>
        <td><b>Serpinski Triangle</b></td>
        <td><b>Triangle A</b></td>
        <td><b>Anthony Hanmer ADH258a</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956997-520e79cc-f385-411c-87ff-85fc2ab64a9b.png" height="220"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957100-01808507-1850-4c47-bcbb-8f438ba6d585.png" height="220"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956323-1d01d244-1a07-4111-86ba-0b94944a1c35.png" height="220"></td>
    </tr>
</table>

### Dragon Shapes

<table>
    <tr>
        <td><b>Dragon Curve</b></td>
        <td><b>McWorter Terdragon</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956392-7bfae987-cc65-4028-be6e-529dc72db6b3.png" height="350"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956758-d5329f78-7259-48cd-afb2-0a449285a5c5.png" height="350"></td>
    </tr>
</table>

### Quadratic Koch Curves

<table>
    <tr>
        <td><b>Koch curve 1</b></td>        
        <td><b>Koch Island 1</b></td>
        <td><b>Koch Island 2</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956638-e8b872f7-836c-4078-8782-fc6a15f12d12.png"></td>        
        <td><img src="https://user-images.githubusercontent.com/9162068/141956899-8025b6e1-2eeb-408a-9a96-ff9fad5fb30c.png"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956915-5239eb4a-1ec5-4909-91b9-6e1214ac6a70.png"></td>
    </tr>
</table>

<table>
    <tr>
        <td><b>Koch curve 2</b></td>
        <td><b>Koch curve 2 (flipped)</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956652-c515be97-9ac3-4625-ac13-3142c17bacdb.png" width="330"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956677-f371fe87-8939-4ac0-bbcd-270b2086433a.png" width="330"></td>
    </tr>
</table>

### Misc Shapes

<table>
    <tr>
        <td><b>Mosaic</b></td>
        <td><b>Anthony Hanmer ADH256a</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956765-c35342f1-53f3-40f4-8ee8-f26bf44451d1.png"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956253-f6fb508d-09b9-42b1-8b88-73bf899a4e47.png"></td>
    </tr>
    <tr>        
        <td><b>Zaikov</b></td>
        <td><b>Unnamed</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957252-253256ee-9b23-4948-bbfd-74bd7ca1e407.png" width="350"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141957183-0d5148a0-10dd-439b-98b3-dfd5c76e5292.png"></td>
    </tr>
    <tr>
        <td><b>Koch Curve</b></td>
        <td><b>Quadratic Snowflake</b></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956685-f748ee84-3ad2-43a1-a1fb-cca27eb51a45.png" width="350"></td>
        <td><img src="https://user-images.githubusercontent.com/9162068/141956957-9c92dcfb-f39f-48e1-9ecc-83a372a141a8.png"></td>
    </tr>
</table>
