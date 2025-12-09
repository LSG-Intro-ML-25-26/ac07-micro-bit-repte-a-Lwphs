def on_button_pressed_a():
    global hand
    hand = hand + 1
    if hand > 3:
        hand = 1
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
        music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
            music.PlaybackMode.UNTIL_DONE)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        basic.show_icon(IconNames.SCISSORS)
        music.play(music.create_sound_expression(WaveShape.SINE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global handCPU
    handCPU = randint(1, 3)
    if handCPU == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
        music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
            music.PlaybackMode.UNTIL_DONE)
    elif handCPU == 2:
        basic.show_icon(IconNames.SQUARE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        basic.show_icon(IconNames.SCISSORS)
        music.play(music.create_sound_expression(WaveShape.SINE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global handCPU
    handCPU = randint(1, 3)
    basic.show_string("CPU")
    if handCPU == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif handCPU == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
    basic.show_string("YOU")
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
    if hand == 1:
        if handCPU == 2:
            basic.show_string("LOSE")
        elif handCPU == 3:
            basic.show_string("WIN")
        else:
            basic.show_string("DRAW")
    elif hand == 2:
        if handCPU == 1:
            basic.show_string("WIN")
        elif handCPU == 3:
            basic.show_string("LOSE")
        else:
            basic.show_string("DRAW")
    else:
        if handCPU == 1:
            basic.show_string("LOSE")
        elif handCPU == 2:
            basic.show_string("WIN")
        else:
            basic.show_string("DRAW")
input.on_button_pressed(Button.B, on_button_pressed_b)

handCPU = 0
hand = 0
hand = 0
basic.show_string("CPU vs YOU")

def on_forever():
    pass
basic.forever(on_forever)
