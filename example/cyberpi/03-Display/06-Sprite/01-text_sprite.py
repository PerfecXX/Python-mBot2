import cyberpi

cyberpi.background.fill(255,255,255)

my_sprite = cyberpi.sprite()
my_sprite2 = cyberpi.sprite()

my_sprite.set_align("top_left")
my_sprite2.set_align("top_left")

my_sprite.set_color(0,0,255)
my_sprite2.set_color(0,255,0)

my_sprite.rotate_to(90)
my_sprite2.rotate_to(90)

my_sprite.move_to(0, 0)
my_sprite2.move_to(0, 0)

my_sprite.draw_text("ฮาาาา")
my_sprite2.draw_text("ไงละ")
my_sprite.set_size(150)
my_sprite2.set_size(150)

cyberpi.screen.render()

