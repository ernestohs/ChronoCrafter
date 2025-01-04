import calendar
from datetime import date, timedelta

def create(year):
    # Basic settings
    width = 1200
    height = 800
    cols = 12  # One column per month
    rows = 31  # Maximum days in a month
    
    cell_width = width / cols
    cell_height = height / rows
    
    # Simple color for all months
    color = "#89B0F0"
    
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
    svg.append(f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">')
    
    current_date = date(year, 1, 1)
    while current_date.year == year:
        # Calculate position
        month = current_date.month
        day = current_date.day
        
        x = (month - 1) * cell_width
        y = (day - 1) * cell_height
        
        # Draw cell
        svg.append(f'<rect x="{x}" y="{y}" width="{cell_width}" height="{cell_height}" '
                  f'fill="{color}" stroke="black" stroke-width="1" fill-opacity="0.5"/>')
        
        # Add text
        text_size = min(cell_width, cell_height) / 3
        text_x = x + cell_width/2
        text_y = y + cell_height/2
        
        # Add date
        date_text = f"{current_date.strftime('%b')} {day}"
        svg.append(f'<text x="{text_x}" y="{text_y}" '
                  f'font-family="Arial" font-size="{text_size}" '
                  f'text-anchor="middle" dominant-baseline="middle">{date_text}</text>')
        
        # Move to next day
        current_date += timedelta(days=1)
    
    svg.append('</svg>')
    
    # Save the file
    filename = f'calendar-{year}.svg'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    
    return filename

calendar_file = create(2025)
print(f"Calendar saved as {calendar_file}")
