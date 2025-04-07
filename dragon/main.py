import tkinter as tk

win = tk.Tk()

def start():
    canvas = tk.Canvas(win, width=500, height=700)
    canvas.create_text(font=('Helvetica', 20), text="""
                                      Chapter one

Griffin was a short blonde-haired boy who was friends with a girl called Clara and a boy called Rory.

“Griffin!” called his Mum, “Come downstairs!”
“Coming Mum!” he yelled back.
Griffin finished getting dressed, rushed downstairs, wolfed down his breakfast, and waved his Mum goodbye as he left for school. As he walked happily down his driveway, he messaged his friends a quick note to meet him in the park before school; he was hoping they would meet him in time for a quick game before the bell.  As he spotted his friends already ahead of him waiting  in the park, he grinned and yelled out to them.
”Come on. Let's play tag!”
“Okay,” Ayzen said “You're it.”
Griffin ran after Clara “You're it.”
“No,” she replied “You're it.”
                       """)

    btn=tk.Button(win, text="next page", command=start )
    btn._pack

