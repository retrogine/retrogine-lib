import pyglet

from retrogine.data_loader import load_data_file

pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)

(sprites, palettes) = load_data_file('../test.data')

window = pyglet.window.Window(width=480*2, height=270*2, resizable=False, fullscreen=False)

main_texture = pyglet.image.Texture.create(480, 256)

sprite1 = sprites[0].get_image(palettes[0])
sprite2 = sprites[0].get_image(palettes[1])


@window.event
def on_draw():
    window.clear()
    main_texture.blit_into(sprite1, 0, 0, 1)
    main_texture.blit_into(sprite2, 0, 32, 1)

    main_texture.blit(0, 7*2, width=480*2, height=256*2)


if __name__ == '__main__':
    pyglet.app.run()
