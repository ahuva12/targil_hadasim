#Input of tower height and width
def input_height_width():
    height = int(input("Enter the height of the tower: "))
    width = int(input("Enter the width of the tower: "))
    return height, width

#Option of a rectangular tower    
def rectangular_tower(height, width):
    if abs(height-width) > 5:
        print("Rectangle area: ", height*width)
    else:
        print("Rectangle scope: ", height*2 + width*2) 
 
#Option of a triangular tower     
def triangular_tower(height, width):
    choice = int(input("enter 1 for print the triangle area, 2 for triangle print: "))
    
    #print the triangle scope
    if choice == 1:
        z = ((0.5*width)**2 + height**2)**0.5     #Pythagoras theorem. z is the equilateral side of the triangle
        print("Triangle scope: ", 2*z + width)

    #print the triangle
    elif choice == 2:
        if width % 2 == 0 or height*2 < width:
            print ("Error! The triangle cannot be printed")
        else:
            middle_rows = list(range(3, width-1, 2))
            num_of_middle_rows = (height-2)//len(middle_rows)
            num_of_first_rows = num_of_middle_rows + (height-2) % len(middle_rows)
            rows = [1] + middle_rows + [width]
            for row in rows:
                if row in middle_rows:
                    if row == middle_rows[0]:
                        for i in range(num_of_first_rows):
                            print(' '*((width-row)//2), '*'*row)
                    else:
                        for i in range(num_of_middle_rows):
                            print(' '*((width-row)//2), '*'*row)
                else:
                    print(' '*((width-row)//2), '*'*row)
    
    else:
        print ("Your input is invalid")
    
    
def main():
    choice = int(input("Please enter 1 for a rectangular tower, 2 for a triangular tower, 3 for exit: "))
    while choice != 3:
        if choice == 1:
            height, width = input_height_width()
            rectangular_tower(height, width)
        elif choice == 2:
            height, width = input_height_width()
            triangular_tower(height, width)
        else:
            print("Your input is invalid. Please enter 1, 2 or 3")
        choice = int(input("Please enter 1 for a rectangular tower, 2 for a triangular tower, 3 for exit: "))


if __name__ == "__main__":
    main()
    
    
#"הדפסת המשולש
#תתבצע בדיקה האם רוחב המשולש הוא מספר זוגי או אם
#רוחבו ארוך ביותר מפי 2 מגובהו, אם כן תודפס למשתמש
#הודעה שלא ניתן להדפיס את המשולש.
#אם רוחבו אי זוגי וקצר מפי 2 מגובהו נדפיס את המשולש
#בצורה הבאה:"
#This instruction is ambiguous.
#It is not clear what to do when the width of the triangle is exactly twice its height

