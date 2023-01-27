# PyGames-PyChess
By: J. Brandon George | darth.data410@gmail.com | twitter: @PyFryDay | medium.com: https://darth-data410.medium.com/ | youtube: https://www.youtube.com/@pyfryday
license found @: PyGames-BattleChess/LICENSE (Apache License Version 2.0 Janurary 2004)

# Details:
This open source project contains elements, source code, graphics, sounds, etc. that support my Medium.com series of post about python3 and pygame. This is meant to be used as a project for understanding how to build a classic chess game. This includes targeting different forms of AI.

This project is structured into named instances of the games source code and assets. Each instance is a copy of the previous named instance, building upon it to a new level of being a more complete game. For example the first named instance is: 01_Intro. The next named instance is 02_Basic_PieceMovement, which is a copy of 01_Intro, yet has added more features, assests, etc.

# Medium.com / YouTube links:
1. Introduction Video: <a href="https://youtu.be/-rJLeR3AHpo">PyGames-PyChess Introduction</a>

<img src="https://i9.ytimg.com/vi/-rJLeR3AHpo/mqdefault.jpg?sqp=CKj70J4G-oaymwEmCMACELQB8quKqQMa8AEB-AHOBYAC7gWKAgwIABABGEwgWyhlMA8=&rs=AOn4CLDVk_khAIyR3W_kbzQwPm9SoUYCfQ">

# 01_Intro
1. Instance Overview 

    This instance is the initial game code and grahics for drawing a chess board, drawing the pieces - correctly - on the chess board, and allowing for the player to press the 'R' key in order to reverse the board / restart the game. 

# 02_Basic_PieceMovement
1. Instance Overview

    This instance is a copy of 01_Intro, yet it is a full build out of a movement rules engine per each piece. This includes all pieces, ability to jump pieces, and tracking pieces via the board. This also includes tracking jumped pieces. This does NOT include castling concepts, "passing pawn" or swapping pawn for another piece when reaching the other side. 

# 03_Advanced_PieceMovements (CURRENTLY IN DEVELOPMENT)
1. Instance Overview

    This instance is a copy of 02_Basic_PieceMovement, targeting development of advanced movemenet concepts like castling, highliting piece movement, including jumps, placing opposite king in check. This includes initial detecting of King being in check, checkmate, passing pawn, trading pawn piece for another, etc. This will have all piece movements, turns, and game play through each side until a checkmate is reached.  

2. Remaining Development:
    1. Finalize Checkmate (Though game will NOT ontinue now, if opposite King has no valid moves, and no other pieces for Kings side does not have any valid moves.)
    2. Finalize Stalemate rules. (No more valid moves for King, when just king is left - 50 move rule - Offer draw logic - etc)
    3. Refactoring to clean up code, scope changes, etc. - Are some issues with the King in check, and also need to finalize King upon King movement restrictions. 

# Upcoming development:
The targeted instance that will follow the completion of 03_Advanced_PieceMovements will be to enable a base computer AI game play. This will be delivered in varrying approaches, and therefore different named instances. Further the initial rounds of Medium.com post are also currently in development. As they are published, each section will be updated to included those post that relate to said section.
