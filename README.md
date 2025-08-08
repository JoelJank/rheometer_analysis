# Rheometer Analysis
This program aims to make the analysis of experimental results of a Rheometer to determine the Mohr-Coulomb diagram and the properties of the given material under investigation.

## Still to do:
- Add error bars
  - Idea: Determine standard deviation from mean of normal stress (easy) -> how to determine the standard deviation of the maximum? Ideas?
  - include error range of Rheometer?
- Figure out what is the best way to present the results
- Talk about what results we want to have a specific look at AND what experiments are yet to be ran.

## Usage
Download the folder "Program". Unpack the folder if necessary. Open the unpacked folder in a Terminal and run 
```
pip install -r "requirements.txt"
```
This will install all necesarry packages. 
All the settings are changed in Folder Settings. 
1. Here, the plot style can be set with the .mplstyle file. This is not necessary. The style can also be set to a standard style of matplotlib.
2. The settings.json determines, with what data and how the program works. Here, most of the changes are done. More on this in the next chapters

When all the settings are correct, just run the program by typing
```
python plotter.py
```
in the CMD in the Program folder.
## File Format
The program is designed to work with excel files only. Use the procedure we used all week when we were in Paris. An example of the formating is represented in the data folder. 
Best practice:
- Run the experiment. In our case the program mostly produced results for 3 consolidation forces. For each of these consolidation forces, there are three areas interesting for us: The areas were we press with less normal stress then when pressing with the consolidation forces.
- Take note that the program is also capable of handling more then 3 areas of interest. We can also look into pressing with more than three different normal stresses
- For each of these consolidation forces, these areas of interest should be copy pasted below each other into one excel sheet.
- **Data necesarry: Time, Normal Stress, Shearstress, Gap (Standard names of the Anton Paar program, do not change)**
- The column for the for example "Normal Stress"  of the second area of interest should be directly below the "Time" column of the first area of interest. Otherwise the program wont work properly. This of course also applies to all other columns.
- The header of each area of interest can be pasted into the excel with no problems
- When providing excel files with multiple sheets for different experiments the program will automatically compare the Mohr Coulomb diagrams for each of the sheets

## Settings in the settings.json file
**DISCLAIMER: DO NOT CHANGE THE VARIABLES LEFT OF THE : IN EACH ROW. OTHERWISE THE PROGRAM WONT WORK**
- *Input_file*: Give the relative or absolute path of the Excel File that should be analysed
- *skip_sheets*: Amount of sheets from the first sheet on in the excel file that should be skipped. Skip every sheets that does not contain the columns labeled with "Time", "Normal Stress", "Shear Stress", "Gap" .
- *ignore_sheets_end*: Amount of sheets in the excel file that should be skipped at the end of the excel file.
- *savgol_window_length*: Amount of points taken into account to calculate the fit with the savgol filter.
- *savgol_polyorder*: Degree of polynomial to fit the data points (More on this: https://medium.com/pythoneers/introduction-to-the-savitzky-golay-filter-a-comprehensive-guide-using-python-b2dd07a8e2ce).
- *output_folder*: Give the relative or absoulute path of the folder the results should be saved in.
- *title_of_experiment*: Informations on the experiment like the material, date, everything you should need to know about the experiment. This will determine the name of the Mohr-Coulomb Graph created
- *plotstyle*: Use the standard plotstyle of matplotlib or set an own plotstyle



Contact: joel.jankowiak@stud.uni-due.de



