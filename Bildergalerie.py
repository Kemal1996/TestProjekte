html = '''
<html>
    <head>
        <title></title>

        <style>
            img {
                width: 400px;
                height: 200px;
                object-fit: cover;
            }
        </style>
    </head>
    <body>
    <h1>Meine Bildergallerie (entnommen aus pixabay.com)</h1>
    <img src='img/4.jpg'>
    <img src='img/4.jpg'>
    <img src='img/4.jpg'>
    <img src='img/4.jpg'>

    <h2>Weitere Bilder</h2>
        <img src='img/0.jpg'>
        <img src='img/1.jpg'>
        <img src='img/2.jpg'>
        <img src='img/3.jpg'>
    </body>
</html>
'''

print(html)

# Write HTML String to file.html
with open('index.html', 'w') as file:
    file.write(html)