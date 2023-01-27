step = 25
u, r, d, l, = (0, -step), (step, 0), (0, step), (-step, 0)

levels = [
    # level 1
{
    'rotation_time' : 5,
    'black_penguin_speed' : 1,
    'movement_steps': [r, r, r, r, r, r, r, r, d, d, l, l, l, d, d, d, d, d, d, d, l, l, l, d, d],
    'level_maze':   # 22 * 14
                    [
                            "WWWWWWWWWWWWWWWWWWWWWW",
                            "W             WWWW   W",
                            "W   WWWWW  W      Wwww",
                            "W   W           WWW  W",
                            "W WWW    WWWW        W",
                            "W   W      W     W   W",
                            "WWWWW      W   WWW  WW",
                            "W  WWW  W WW   W  WwwW",
                            "W       W       W W  W",
                            "W WW        WWWWW W  W",
                            "W W      W W         W",
                            "W      WWWW    WWW   W",
                            "W  E   W          W  W",
                            "WWWWWWWWWWWWWWWWWWWWWW",
                        ],


    } ,
# level 2
{
    'rotation_time' : 2,
    'black_penguin_speed' : 1,
    'movement_steps': [r, r, r, r, r, r, d, d, r, r, r, r, r, r, d, d, d, l, d, d, l, l, d, d, r, r, r, r, r, r, r, r, d, d],

    'level_maze':   # 22 * 14
                    [
                        "WWWWWWWWWWWWWWWWWWWWWW",
                        "W        WWWWWWWWWW  W",
                        "W                WW  W",
                        "W WWWWW  W     WWWW  W",
                        "W  WWWWWWWWWW        W",
                        "W   W      WW        W",
                        "W   W          WWWWWWW",
                        "W   WWW   WW   W     W",
                        "W       W    W W     W",
                        "W  WW   W  WWWWW     W",
                        "W W     WW           W",
                        "W  W   WWWW    WWW   W",
                        "W    E W         W E W",
                        "WWWWWWWWWWWWWWWWWWWWWW",
                    ],


    } ,
# level 3
{
    'rotation_time' : 2,
    'black_penguin_speed' : 2,
    'movement_steps': [d, d, d, d, d, d, d, r, r, r, r, r, d, d, d, d, r, r, r, r, r, r, r, u, u, r, r, r, r, r, d, d],
    'level_maze':   # 22 * 14
                    [
                            "WWWWWWWWWWWWWWWWWWWWWW",
                            "W  WWWW          wwwwW",
                            "W     WWWW       W   W",
                            "W   W          WWWW  W",
                            "W  WWW   WWWW        W",
                            "W   W      W  W      W",
                            "W   W      W   WWWwwWW",
                            "W   WWWW  WW   W  WwwW",
                            "W      W        W W  W",
                            "W WW   W     WWWW W  W",
                            "W W      W           W",
                            "W      WWWW    WWW   W",
                            "W                W E W",
                            "WWWWWWWWWWWWWWWWWWWWWW",
                        ],


    } ,

# level 4
{
    'rotation_time' : 2,
    'black_penguin_speed' : 3,
    'movement_steps': [r, r, r, r, d, d, d, d, r, r, r, r, r, d, d, d, d, r, d, d, d, l, l, l],
    'level_maze':   # 22 * 14
                    [
                            "WWWWWWWWWWWWWWWWWWWWWW",
                            "W     WWWW           W",
                            "W            wwwwW   W",
                            "W  W           WWWW  W",
                            "W WWW    WWWW        W",
                            "W   W      W  W      W",
                            "W   W      W   WWW  WW",
                            "W   WWWWW  WW  W     W",
                            "W      W    W        W",
                            "W WW   W    WWWWW    W",
                            "W W      W           W",
                            "W W   WWWWW    WWWW  W",
                            "W     W E         W  W",
                            "WWWWWWWWWWWWWWWWWWWWWW",
                        ],


    } ,
# level 5
{
    'rotation_time' : 2,
    'black_penguin_speed' : 4,
    'movement_steps': [r, r, r, r, d, d, r, r, r, r, r, r, r, r, r, d, r, r, r, r, r, d, d, d, d, d, d, d, d],
    'level_maze':   # 22 * 14
                    [
                            "WWWWWWWWWWWWWWWWWWWWWW",
                            "W     WWWW           W",
                            "W     WWWW       W   W",
                            "W   W          WWWW  W",
                            "W WWW    WWWW        W",
                            "W   W      W  W      W",
                            "W   W      W   WWW  WW",
                            "W   WWW W WW   W  W  W",
                            "W      W    W   W W  W",
                            "W WW   W    WWWWW W  W",
                            "W W      W W         W",
                            "W  W   WWWW    WWW   W",
                            "W     W          W E W",
                            "WWWWWWWWWWWWWWWWWWWWWW",

                    ],


    },

]






































# levels = [
#     # level 1
# {
#     'rotation_time' : 5,
#     'black_penguin_speed' : 1,
#     'level_maze':   # 22 * 14
#                     [
#                             "WWWWWWWWWWWWWWWWWWWWWW",
#                             "W     WWWW           W",
#                             "W     WWWW       W   W",
#                             "W   W          WWWW  W",
#                             "W WWW    WWWW        W",
#                             "W   W      W  W      W",
#                             "W   W      W   WWW  WW",
#                             "W   WWW W WW   W  W  W",
#                             "W      W    W   W W  W",
#                             "W WW   W    WWWWW W  W",
#                             "W W      W W         W",
#                             "W  W   WWWW    WWW   W",
#                             "W     W          W E W",
#                             "WWWWWWWWWWWWWWWWWWWWWW",
#                         ],
#
#
#     } ,
# # level 2
# {
#     'rotation_time' : 2,
#     'black_penguin_speed' : 10,
#     'level_maze':   # 22 * 14
#                     [
#                             "WWWWWWWWWWWWWWWWWWWWWW",
#                             "W     WWWW           W",
#                             "W     WWWW       W   W",
#                             "W   W          WWWW  W",
#                             "W WWW    WWWW        W",
#                             "W   W      W  W      W",
#                             "W   W      W   WWW  WW",
#                             "W   WWW W WW   W  W  W",
#                             "W      W    W   W W  W",
#                             "W WW   W    WWWWW W  W",
#                             "W W      W W         W",
#                             "W  W   WWWW    WWW   W",
#                             "W     W          W E W",
#                             "WWWWWWWWWWWWWWWWWWWWWW",
#                         ],
#
#
#     } ,
# # level 3
# {
#     'rotation_time' : 2,
#     'black_penguin_speed' : 2,
#     'level_maze':   # 22 * 14
#                     [
#                             "WWWWWWWWWWWWWWWWWWWWWW",
#                             "W     WWWW           W",
#                             "W     WWWW       W   W",
#                             "W   W          WWWW  W",
#                             "W WWW    WWWW        W",
#                             "W   W      W  W      W",
#                             "W   W      W   WWW  WW",
#                             "W   WWW W WW   W  W  W",
#                             "W      W    W   W W  W",
#                             "W WW   W    WWWWW W  W",
#                             "W W      W W         W",
#                             "W  W   WWWW    WWW   W",
#                             "W     W          W E W",
#                             "WWWWWWWWWWWWWWWWWWWWWW",
#                         ],
#
#
#     } ,
#
# # level 4
# {
#     'rotation_time' : 2,
#     'black_penguin_speed' : 2,
#     'level_maze':   # 22 * 14
#                     [
#                             "WWWWWWWWWWWWWWWWWWWWWW",
#                             "W     WWWW           W",
#                             "W     WWWW       W   W",
#                             "W   W          WWWW  W",
#                             "W WWW    WWWW        W",
#                             "W   W      W  W      W",
#                             "W   W      W   WWW  WW",
#                             "W   WWW W WW   W  W  W",
#                             "W      W    W   W W  W",
#                             "W WW   W    WWWWW W  W",
#                             "W W      W W         W",
#                             "W  W   WWWW    WWW   W",
#                             "W     W          W E W",
#                             "WWWWWWWWWWWWWWWWWWWWWW",
#                         ],
#
#
#     } ,
# # level 5
# {
#     'rotation_time' : 2,
#     'black_penguin_speed' : 2,
#     'level_maze':   # 22 * 14
#                     [
#                             "WWWWWWWWWWWWWWWWWWWWWW",
#                             "W     WWWW           W",
#                             "W     WWWW       W   W",
#                             "W   W          WWWW  W",
#                             "W WWW    WWWW        W",
#                             "W   W      W  W      W",
#                             "W   W      W   WWW  WW",
#                             "W   WWW W WW   W  W  W",
#                             "W      W    W   W W  W",
#                             "W WW   W    WWWWW W  W",
#                             "W W      W W         W",
#                             "W  W   WWWW    WWW   W",
#                             "W     W          W E W",
#                             "WWWWWWWWWWWWWWWWWWWWWW",
#                         ],
#
#
#     } ,
#
# ]