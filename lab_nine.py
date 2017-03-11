file = input("Enter input file: ")

filename = open(file, "r")

place_dict = {} # to obtain a dictionary of YEG, YYC, YVR information from the input files. Keys are YEG, YYC, and YVR, whereas everything else are a list of values
    
for line in filename:
    x = line.split(';') # split each line at the colon 
    if x[0] in place_dict: # if first line is the key in dict, you append all values to that key  
        place_dict[x[0]].append(x[1:])
    else:
        place_dict[x[0]] = [x[1:]]
     
filename.close()

# all this BS is the title, borders, and pics so you don't have to write it multiple times
title = "<html><body><h1>Query Results</h1>"
first_line = "<h2>From city: Calgary</h2>"
second_line = "<h2>From city: Edmonton</h2>"
third_line = "<h2>From city: Vancouver</h2></body></html>"
star = '''<img src ="star-full.png" style = 'width:20px;height:20px'/>'''
half_star = '''<img src ="star-half.png" style = 'width:20px;height:20px'/>'''
empty_star = '''<img src ="star-empty.png" style = 'width:20px;height:20px'/>'''


file_ext = file[:-5] + ".html" # to modify filename from .data to .html
website = open(file_ext, "w")


for i in range(len(place_dict['YEG'])): # to create a crap ton of webpages if they click on More... for edmonton
    string_name = 'next_pageE' + str(i) + '.html'
    star_drawing4 = star * int(float(place_dict['YEG'][i][1]))
    yeg_stars = int(float(place_dict['YEG'][i][1]))
    website2 = open(string_name, 'w') # the next page of the website if they choose to click on more
    # to draw the stars for each review
    if float(place_dict['YEG'][i][1]) - int(float(place_dict['YEG'][i][1])) != 0:
        star_drawing4 += half_star
        yeg_stars += 1
    else:
        star_drawing4 = star * int(float(place_dict['YEG'][i][1]))
        
    while yeg_stars < 5:
        star_drawing4 += empty_star
        yeg_stars +=1
        
    website2.write(title)
    website2.write(second_line)
    picture_string1 = '''<img src = " '''+ str(place_dict['YEG'][i][3]) + ''' " />'''
    website2.write(picture_string1)
    website2.write('<br>' + str(place_dict['YEG'][i][5]) + '</br>')
    website2.write('<p></p>')
    website2.write('</body></html>')
    bullet_list = '<ul><li>' + str(place_dict['YEG'][i][0]) + '</li><li>Reviews: ' + str(star_drawing4) + '(' + str(place_dict['YEG'][i][1]) + ')</li><li>Price per night: ' + str(place_dict['YEG'][i][2]) + '</li><li>' + '''<a href=" ''' + str(place_dict['YEG'][i][4]) + ''' ">''' + str(place_dict['YEG'][i][4])+ '''</a></li><li>Phone: '''+ str(place_dict['YEG'][i][6]) + '</li><li>Address: ' + str(place_dict['YEG'][i][7]) + '</li></ul>'
    website2.write(bullet_list)
    website2.close()

for i in range(len(place_dict['YYC'])): # this for all webapages if they click on More...for Calgary
    string_name = 'next_pageC' + str(i) + '.html'
    star_drawing5 = star * int(float(place_dict['YYC'][i][1]))
    yyc_stars = int(float(place_dict['YYC'][i][1]))
    website3 = open(string_name, 'w')
    
    if float(place_dict['YYC'][i][1]) - int(float(place_dict['YYC'][i][1])) != 0:
        star_drawing5 += half_star
        yyc_stars += 1
    else:
        star_drawing5 = star * int(float(place_dict['YYC'][i][1])) 
        
    while yyc_stars < 5:
        star_drawing5 += empty_star
        yyc_stars +=1    
        
    website3.write(title)
    website3.write(first_line)
    picture_string2 = '''<img src = " ''' + str(place_dict['YYC'][i][3]) +''' " />'''
    website3.write(picture_string2)
    website3.write('<br>' + str(place_dict['YYC'][i][5]) + '</br>')
    website3.write('<p></p>')
    website3.write('</body></html>')
    bullet_list2 = '<ul><li>' + str(place_dict['YYC'][i][0]) + '</li><li>Reviews: ' + str(star_drawing5) + '(' + str(place_dict['YYC'][i][1]) + ')</li><li>Price per night: ' + str(place_dict['YYC'][i][2]) + '</li><li>' + '''<a href=" ''' + str(place_dict['YYC'][i][4]) + ''' ">''' + str(place_dict['YYC'][i][4]) + '''</a></li><li>Phone: '''+ str(place_dict['YYC'][i][6]) + '</li><li>Address: ' + str(place_dict['YYC'][i][7]) + '</li></ul>'
    website3.write(bullet_list2)    
    website3.close()
    
if 'YVR' in place_dict: # if they key is in the place_dict and it exists, these are for the webpages if they click on More...for anything in the Vancouver table
    for i in range(len(place_dict['YVR'])):
        string_name = 'next_pageV' + str(i) + '.html'
        star_drawing6 = star * int(float(place_dict['YVR'][i][1]))
        yvr_stars = int(float(place_dict['YVR'][i][1]))
        website4 = open(string_name, 'w')
        
        if float(place_dict['YVR'][i][1]) - int(float(place_dict['YVR'][i][1])) != 0:
            star_drawing6 += half_star
            yvr_stars += 1
        else:
            star_drawing6 = star * int(float(place_dict['YVR'][i][1]))
        
        while yvr_stars < 5:
            star_drawing6 += empty_star
            yvr_stars +=1        
            
        website4.write(title)
        website4.write(third_line)
        picture_string3 = '''<img src = " ''' + str(place_dict['YVR'][i][3]) + ''' " />'''
        website4.write(picture_string3)
        website4.write('<br>' + str(place_dict['YVR'][i][5]) + '</br>')
        website4.write('<p></p>')
        bullet_list3 = '<ul><li>' + str(place_dict['YVR'][i][0]) + '</li><li>Reviews: ' + str(star_drawing6) + '(' + str(place_dict['YVR'][i][1]) + ')</li><li>Price per night: ' + str(place_dict['YVR'][i][2]) + '</li><li>' + '''<a href=" ''' + str(place_dict['YVR'][i][4]) + ''' ">''' + str(place_dict['YVR'][i][4]) + '''</a></li><li>Phone: '''+ str(place_dict['YVR'][i][6]) + '</li><li>Address: ' + str(place_dict['YVR'][i][7]) + '</li></ul>'
        website4.write(bullet_list3)        
        website4.close()
else:
    None

# draws the table border with the categories
table_border= '''<table border = "2" ><tr><td>''' + str(place_dict['City'][0][0]) + "</td><td>" + str(place_dict['City'][0][1]) + "</td><td>" + str(place_dict['City'][0][2]) +"</td><td>Details</td></tr><tr>"

table_string1 = '' 
j = 0 # for the information within the table regarding Calgary
for i in range(len(place_dict['YYC'])): 
    star_drawing1 = star * int(float(place_dict['YYC'][i][1]))
    yyc_stars1 = int(float(place_dict['YYC'][i][1]))
    
    if float(place_dict['YYC'][i][1]) - int(float(place_dict['YYC'][i][1])) != 0:
        star_drawing1 += half_star
        yyc_stars1 += 1
    else:
        star_drawing1 = star * int(float(place_dict['YYC'][i][1])) 
        
    while yyc_stars1 < 5:
        star_drawing1 += empty_star
        yyc_stars1 +=1    
        
    table_string1 += '<tr><td>' + str(place_dict['YYC'][i][j]) + '</td><td>' + str(star_drawing1) + '(' + str(place_dict['YYC'][i][j+1]) + ')</td><td>' + str(place_dict['YYC'][i][j+2]) + '''</td><td><a href ="next_pageC''' + str(i) + '''.html">More...<a/></td></tr>'''  

table_string2 = '' 
j = 0 # for the information within the table regarding Edmonton
for i in range(len(place_dict['YEG'])): # index number of elements in YEG
    star_drawing2 = star * int(float(place_dict['YEG'][i][1]))
    yeg_stars1 = int(float(place_dict['YEG'][i][1]))
    
    if float(place_dict['YEG'][i][1]) - int(float(place_dict['YEG'][i][1])) != 0:
        star_drawing2 += half_star
        yeg_stars1 += 1
    else:
        star_drawing2 = star * int(float(place_dict['YEG'][i][1])) 
    
    while yeg_stars1 < 5:
        star_drawing2 += empty_star
        yeg_stars1 +=1    
            
    table_string2 += '<tr><td>' + str(place_dict['YEG'][i][j]) + '</td><td>' + str(star_drawing2) + '(' + str(place_dict['YEG'][i][j+1]) + ')</td><td>' + str(place_dict['YEG'][i][j+2]) + '''</td><td><a href ="next_pageE''' + str(i) +'''.html">More...<a/></td></tr>'''

table_string3 = ''     
if 'YVR' in place_dict: # if the key for Vancouver exists, draw the information for Vancouver onto the table
    j = 0
    for i in range(len(place_dict['YVR'])): # index number of elements in YVR
        star_drawing3 = star * int(float(place_dict['YVR'][i][1]))
        yvr_stars1 = int(float(place_dict['YVR'][i][1]))
        
        if float(place_dict['YVR'][i][1]) - int(float(place_dict['YVR'][i][1])) != 0:
            star_drawing3 += half_star
            yvr_stars1 += 1
        else:
            star_drawing3 = star * int(float(place_dict['YVR'][i][1]))
            
        while yvr_stars1 < 5:
            star_drawing3 += empty_star
            yvr_stars1 +=1        
                
        table_string3 += '<tr><td>' + str(place_dict['YVR'][i][j]) + '</td><td>' + str(star_drawing3) + '(' + str(place_dict['YVR'][i][j+1]) + ')</td><td>' + str(place_dict['YVR'][i][j+2]) + '''</td><td><a href ="next_pageV''' +str(i) + '''.html">More...<a/></td></tr>'''
else:
    None
# writing everything onto the html file
website.write(title)
website.write(first_line)
website.write(table_border)
website.write(table_string1)
website.write('</table>')
website.write(second_line)
website.write(table_border)
website.write(table_string2)
website.write('</table>')
if 'YVR' in place_dict: # write the table only if Vancouver exists in dictionary
    website.write(third_line)
    website.write(table_border)
    website.write(table_string3)
    website.write('</table>')
else:
    None

website.close()


