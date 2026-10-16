import struct
import zlib
import os

width = 512
height = 512

def create_tiziqiang_icon():
    # 512x512 RGBA
    raw_data = bytearray()
    
    # Background gradient: deep dark slate #0b0f19 to #0f172a
    # Ladder & Wall emblem with cyan-blue gradient #06b6d4 to #3b82f6
    for y in range(height):
        raw_data.append(0) # filter type 0
        ny = y / float(height)
        for x in range(width):
            nx = x / float(width)
            
            # Base background
            # Rounded corner check for app icon (radius ~ 96px)
            r = 96
            in_corner = False
            dx, dy = 0, 0
            if x < r and y < r:
                dx, dy = r - x, r - y
                in_corner = (dx*dx + dy*dy) > (r*r)
            elif x > width - r and y < r:
                dx, dy = x - (width - r), r - y
                in_corner = (dx*dx + dy*dy) > (r*r)
            elif x < r and y > height - r:
                dx, dy = r - x, y - (height - r)
                in_corner = (dx*dx + dy*dy) > (r*r)
            elif x > width - r and y > height - r:
                dx, dy = x - (width - r), y - (height - r)
                in_corner = (dx*dx + dy*dy) > (r*r)
            
            if in_corner:
                raw_data.extend([0, 0, 0, 0])
                continue
                
            # Background dark tech blue
            bg_r = int(11 + 6 * ny)
            bg_g = int(15 + 10 * ny)
            bg_b = int(25 + 20 * ny)
            bg_a = 255
            
            # Outer subtle glow / border
            border_dist = min(x, width - 1 - x, y, height - 1 - y)
            if border_dist < 4:
                bg_r = int(bg_r * 0.7 + 59 * 0.3)
                bg_g = int(bg_g * 0.7 + 130 * 0.3)
                bg_b = int(bg_b * 0.7 + 246 * 0.3)

            # Draw "Ladder" (梯子) transitioning into "Wall / Shield" (墙)
            # Center is (256, 256). Emblem bounds roughly x in [128, 384], y in [100, 412]
            # Left rail: x in [150, 180], y in [120, 392]
            # Right rail: x in [332, 362], y in [120, 392]
            # 4 Rungs: y around 165, 225, 285, 345, thickness 22, x in [165, 347]
            # Central shield accent: diamond/hexagon motif in the center
            
            is_emblem = False
            emb_factor = 0.0 # for color mixing
            
            # Left rail
            if 150 <= x <= 180 and 120 <= y <= 392:
                is_emblem = True
                emb_factor = 1.0 - (y - 120) / 272.0
            # Right rail
            elif 332 <= x <= 362 and 120 <= y <= 392:
                is_emblem = True
                emb_factor = 1.0 - (y - 120) / 272.0
            # Rungs
            elif (150 <= x <= 362):
                for rung_y in [165, 225, 285, 345]:
                    if abs(y - rung_y) <= 12:
                        is_emblem = True
                        emb_factor = 1.0 - (rung_y - 120) / 272.0
                        break
            
            # Center subtle tech core / ascending signal bar
            if 244 <= x <= 268 and 140 <= y <= 370:
                is_emblem = True
                emb_factor = 0.8
                
            if is_emblem:
                # Vibrant Cyan #06b6d4 to Electric Blue #3b82f6 to Indigo #6366f1
                # emb_factor: 1 at top (cyan), 0 at bottom (electric blue/indigo)
                fg_r = int(6 + (99 - 6) * (1.0 - emb_factor))
                fg_g = int(182 + (102 - 182) * (1.0 - emb_factor))
                fg_b = int(212 + (241 - 212) * (1.0 - emb_factor))
                raw_data.extend([fg_r, fg_g, fg_b, 255])
            else:
                raw_data.extend([bg_r, bg_g, bg_b, bg_a])

    def chunk(tag, data):
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)

    ihdr = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    idat = zlib.compress(bytes(raw_data), 9)
    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', ihdr) + chunk(b'IDAT', idat) + chunk(b'IEND', b'')
    
    with open('/Users/goldentay/Desktop/tiziqiang.blog/preview-icon.png', 'wb') as f:
        f.write(png)
        
    print("Successfully generated preview-icon.png")

create_tiziqiang_icon()
