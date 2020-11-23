from pico2d import *
import gfw
import player
import generator
import bg
import highscore

STATE_IN_GAME, STATE_GAME_OVER = range(2) # 각각 0과 1 대입한 것과 동일

def collides_distance(a, b): #거리충돌 - 원형
	ax, ay = a.pos
	bx, by = b.pos
	radius_sum = a.radius + b.radius
	distance_sq = (ax-bx)**2 + (ay-by)**2 #루트 대신 거리 제곱
	return distance_sq < radius_sum**2

def check_collision(): # 충돌
	global state
	for m in gfw.world.objects_at(gfw.layer.missile):
		if collides_distance(player, m):
			wav_explosion.play()
			gfw.world.remove(m)
			dead = player.decrease_life()
			if dead:
				end_game()

def start_game():
	global state
	if state != STATE_GAME_OVER:
		return 
	player.reset()
	gfw.world.clear_at(gfw.layer.missile)
	gfw.world.remove(highscore)
	
	state = STATE_IN_GAME

	global score
	score = 0

	music_bg.repeat_play()

def end_game():
	global state
	print('Dead')
	state = STATE_GAME_OVER
	music_bg.stop()

	highscore.add(score)
	gfw.world.add(gfw.layer.ui, highscore)


def enter():
	gfw.world.init(['bg', 'missile', 'player','ui'])
	player.init()
	gfw.world.add(gfw.layer.player, player)
	bg.init()
	gfw.world.add(gfw.layer.bg, bg)

	global game_over_image
	game_over_image = gfw.image.load('res/game_over.png')

	global font
	font = gfw.font.load('res/ConsolaMalgun.ttf', 40)

	global music_bg, wav_item, wav_explosion
	music_bg = load_music('res/background.mp3')
	wav_item = load_wav('res/item.wav') #소리를 짧게 낼 때는 wav
	wav_explosion = load_wav('res/explosion.wav')

	highscore.load()

	global state
	state = STATE_GAME_OVER
	start_game()

def exit():
	global music_bg, wav_item, wav_explosion
	del music_bg
	del wav_explosion
	del wav_item

def update():
	if state != STATE_IN_GAME:
		return
	global score
	score += gfw.delta_time
	gfw.world.update()
	generator.update(score) #점수에 따라 난이도 조절
	check_collision()

def draw():
	gfw.world.draw()
	score_pos = 30, get_canvas_height() - 30
	font.draw(*score_pos, 'Score: %.1f' % score, (255,255,255))
	if state == STATE_GAME_OVER:
		center = get_canvas_width() // 2, get_canvas_height() * 2 // 3
		game_over_image.draw(*center)

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			gfw.pop()
		elif e.key == SDLK_RETURN:
			start_game()

	player.handle_event(e)

if __name__ == '__main__':
	gfw.run_main()