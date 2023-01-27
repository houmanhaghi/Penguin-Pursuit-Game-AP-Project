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


    },

# level 2
{
    'rotation_time' : 4,
    'black_penguin_speed' : 1,
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


    },

# level 3
{
    'rotation_time' : 3,
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


    },

# level 4
{
    'rotation_time' : 2,
    'black_penguin_speed' : 3,
    'movement_steps': [r, r, r, r, r, r, d, r, r, r, r, r, r, d, d, d, d, d, l, d, l, l, d, d, r, r, r, r, r, r, r, r, r, d],
    'level_maze':   # 22 * 14
                    [
                        "WWWWWWWWWWWWWWWWWWWWWW",
                        "W        WWWWWWWWWW  W",
                        "W                WW  W",
                        "W WWWWW        WWWW  W",
                        "W  WWWWWWWWWW        W",
                        "W   W      WW        W",
                        "W   W          WWWWWWW",
                        "W   WWW   WW   W     W",
                        "W       W    W W     W",
                        "W  WW   W  WWWWW     W",
                        "W W     WW           W",
                        "W  W   WWWW    WWW   W",
                        "W      W         W E W",
                        "WWWWWWWWWWWWWWWWWWWWWW",
                    ],


    },

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

# level 6
{
    'rotation_time' : 2,
    'black_penguin_speed' : 5,
    'movement_steps': [d, r, r, r, r, r, r, d, d, d, d, r, r, d, d, r, r, r, r, r, r, r, r, d, r],
    'level_maze':   # 22 * 14
                    [
                            "WWWWWWWWWWWWWWWWWWWWWW",
                            "W   WWWWWWWWW    wwwwW",
                            "W       WW  W    W   W",
                            "W   W       W  WWWW  W",
                            "W  WWW   WWWW  W     W",
                            "W   W      W  WW     W",
                            "W   W      W    WWwwWW",
                            "W   WWWW  WW      WwwW",
                            "W      W          W  W",
                            "W WW  W   WWWW WW  E W",
                            "W W      W     W     W",
                            "W      WWWW    WWW   W",
                            "W                W   W",
                            "WWWWWWWWWWWWWWWWWWWWWW",
                        ],


    },

# level 7
{
    'rotation_time' : 2,
    'black_penguin_speed' : 6,
    'movement_steps': [d, d, d, d, d, d, d, r, r, r, r, d, d, d, d, r, r, r, r, u, r, r, d, r, r, r, u, u, u, u, r, r, r, d, r, r, u, u, u, u, u, u, u],
    'level_maze':   # 22 * 14
                    [
                            "WWWWWWWWWWWWWWWWWWWWWW",
                            "W   WWWWWWWWW    wwwwW",
                            "W       WW  W    W E W",
                            "W   W       W  W WW  W",
                            "W  WWW   WWWW  W     W",
                            "W   W      W  WW  W  W",
                            "W   W      W    WWw WW",
                            "W   WWWW  WW      W wW",
                            "W      W  W       W  W",
                            "W WW  W   WWWW WW    W",
                            "W W   W  W   W W     W",
                            "W     WWW   WW WWW   W",
                            "W         W      W   W",
                            "WWWWWWWWWWWWWWWWWWWWWW",
                        ],


    },

# level 8
{
    'rotation_time' : 2,
    'black_penguin_speed' : 7,
    'movement_steps': [d, d, d, d, d, d, d, r, r, r, r, d, d, d, d, r, r, r, r, u, r, r, d, r, r, r, u, u, u, u, l, u, u, u, u, u, u, l, l, d, l, l, l, d, d],
    'level_maze':   # 22 * 14
                    [
                            "WWWWWWWWWWWWWWWWWWWWWW",
                            "W   WWWWWWWWW    wwwwW",
                            "W   W   WW       W   W",
                            "W   W       W  W WW  W",
                            "W  WWW   WWWW  W     W",
                            "W   W    E W  WW  W  W",
                            "W   W      W    WWw WW",
                            "W   WWWW  WW      W wW",
                            "W      W  W       W  W",
                            "W WW  W   WWWW WW    W",
                            "W W   W  W   W W     W",
                            "W     WWW   WW WWW   W",
                            "W         W      W   W",
                            "WWWWWWWWWWWWWWWWWWWWWW",
                        ],


    },

# level 9
{
    'rotation_time' : 2,
    'black_penguin_speed' : 8,
    'movement_steps': [d, d, d, r, r, r, r, r, r, r, u, r, r, r, u, r, r, d, d, d, d, r, d, d, l, d, d, l, l, d, l],
    'level_maze':   # 22 * 14
                    [
                            "WWWWWWWWWWWWWWWWWWWWWW",
                            "W   WWWWWWWWW    wwwwW",
                            "W   W   WW       W   W",
                            "W  WWW      W  W WW  W",
                            "W        WWWW  W     W",
                            "W   W      W  WW  W  W",
                            "W   W      W    WWw WW",
                            "W   WWWW  WWWW    W wW",
                            "W      W  W       W  W",
                            "W WW  W   WWW WWW    W",
                            "W W   W  W      W    W",
                            "W    WWWW E WW WWW   W",
                            "W    W    W      W   W",
                            "WWWWWWWWWWWWWWWWWWWWWW",
                        ],


    },

# level 10
{
    'rotation_time' : 1,
    'black_penguin_speed' : 9,
    'movement_steps': [d, d, d, d, d, r, r, d, d, r, r, d, d, d, r, d, r, r, r, u, r, r, u, r, r, u, u, r, r, r, r, d, r, r, u, u, u, u, u, l, l, l, u, u, u, l, l, l, l, l, d, d, l, d, d, l, l, u, l, l, u, u, l],
    'level_maze':   # 22 * 14
                    [
                            "WWWWWWWWWWWWWWWWWWWWWW",
                            "W   WWWWWWW      wwwwW",
                            "W   WE  WW  W    W   W",
                            "W  WWW WW   W  W WW  W",
                            "W   W    W WW  W     W",
                            "W  WWWW    W  WW  W  W",
                            "W   W      W  W WWw WW",
                            "W   WWWW  WWWW    W wW",
                            "W      W  W       W  W",
                            "W WW  W   WWW WWW    W",
                            "W W   W  W      W    W",
                            "W      WW   WW WWW   W",
                            "W    W    W      W   W",
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