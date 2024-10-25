import cyberpi

pixel_list = ["music","picture","video","clock","play","pause","next","prev","sound","temperature","light","motion","home","gear","list","right","wrong","shut_down","refresh","trash_can","download","sunny","cloudy","rain","snow","train","rocket","car","truck","droplet","distance","fire","magnetic","gas","vision","color","overcast","foggy","sandstorm"]

my_sprite = cyberpi.sprite()
my_sprite.draw_pixel(pixel_list[0])
my_sprite.set_size(200)
cyberpi.screen.render()
