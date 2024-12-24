from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from game_logic import TicTacToe, MCTS

app = FastAPI()
game = TicTacToe()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return generate_readme()

@app.get("/clickCell/{cell_index}")
async def click_cell(cell_index: int):
    if game.make_move(cell_index, TicTacToe.CROSS_CELL):
        if game.current_winner:
            return RedirectResponse(url="/")
        ai = MCTS(game)
        ai_move = ai.get_move()
        game.make_move(ai_move, TicTacToe.NOUGHT_CELL)
    return RedirectResponse(url="/")

def generate_readme():
    board_images = [f"https://your-backend-url/static/assets/rect_{cell}.svg" for cell in game.board]
    board_ctas = [f"https://your-backend-url/clickCell/{i}" for i in range(9)]
    readme_content = f"""
# Tic-Tac-Toe
Tic-tac-toe game from markdown file.

# Disclaimer
### I'm using a free tier cloud server for backend, since it's free tier, the server will shutdown after some amount of inactivity, so If you don't see the tic-tac-toe board rendered below, wait for a 30-45 seconds and refresh the page.

* You are player 'X' and player 'O' is computer.
* Press any empty box to begin the game play or click 'Let computer play first' button.
* Single game play shared with the entire internet so if you see a finished game click 'restart'. [Read more](https://github.com/sridhar-sp/tic-tac-toe-backend#backstory)
* For every move the screen reload to render the board. Have fun.
* ```Disclaimer: This project uses a free-tier server, so after 15 minutes of inactivity, the server goes to sleep. If you don't see the tic-tac-toe board rendered, then it means the server is sleeping. Try again in 1 minute. The server should be up and running.```

<br/>
[![image-0]][cta-0] [![image-1]][cta-1] [![image-2]][cta-2]<br/>
[![image-3]][cta-3] [![image-4]][cta-4] [![image-5]][cta-5]<br/>
[![image-6]][cta-6] [![image-7]][cta-7] [![image-8]][cta-8]

[![play-button-image]][play-button-image-cta]

### Activities

![activities]

[image-0]: {board_images[0]}
[image-1]: {board_images[1]}
[image-2]: {board_images[2]}
[image-3]: {board_images[3]}
[image-4]: {board_images[4]}
[image-5]: {board_images[5]}
[image-6]: {board_images[6]}
[image-7]: {board_images[7]}
[image-8]: {board_images[8]}

[cta-0]: {board_ctas[0]}
[cta-1]: {board_ctas[1]}
[cta-2]: {board_ctas[2]}
[cta-3]: {board_ctas[3]}
[cta-4]: {board_ctas[4]}
[cta-5]: {board_ctas[5]}
[cta-6]: {board_ctas[6]}
[cta-7]: {board_ctas[7]}
[cta-8]: {board_ctas[8]}

[play-button-image]: https://your-backend-url/static/assets/computer_start_button.svg
[play-button-image-cta]: https://your-backend-url/clickCell/computer_start

[activities]: https://your-backend-url/static/assets/activities.svg
"""
    with open("README.md", "w") as f:
        f.write(readme_content)
    return readme_content

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)