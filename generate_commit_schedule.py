from datetime import datetime, timedelta

# Define the "can I has job?" grid (7 rows, variable-width)
letter_grid = [
    " #   #  ##   #  # #  #   #   ###  #  ## ",
    "# # # # # #  #  # # # # # #   #  # # # #",
    "#   # # # #  #  # # # # #     #  # # # #",
    "#   ### # #  #  ### ###  #    #  # # ## ",
    "#   # # # #  #  # # # #   #   #  # # # #",
    "# # # # # #  #  # # # # # #   #  # # # #",
    " #  # # # #  #  # # # #  #   ##   #  ## ",
]

# Define start date (first Sunday of the year)
start_date = datetime(2025, 3, 16)  # Adjust this for different years

commit_dates = []

# Iterate over the grid and map to GitHub contribution days
for col, pixels in enumerate(zip(*letter_grid)):  # Transpose grid
    for row, pixel in enumerate(pixels):
        if pixel == "#":  # If pixel is "on"
            commit_day = start_date + timedelta(weeks=col, days=row)
            commit_dates.append(commit_day.strftime("%Y-%m-%d"))


# Print commit dates
print("Commit Dates:")
print("\n".join(commit_dates))

with open("dates.txt", "w") as f:
    f.write("\n".join(commit_dates))
