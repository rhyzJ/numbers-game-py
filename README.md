<h1>Dice Game</h1>
<p>This is a simple Python-based dice-rolling game where players take turns rolling a die to reach a target score.</p>
    
  <h2>How to Play</h2>
    <ol>
        <li>The game supports 2 to 4 players.</li>
        <li>Each player takes turns rolling a six-sided die.</li>
        <li>If a player rolls a 1, they lose all points for that round, and their turn ends.</li>
        <li>Players can choose to roll again or keep their score.</li>
        <li>The first player to reach <strong>50 points</strong> wins the game.</li>
    </ol>
    
   <h2>Installation</h2>
    <p>Ensure you have Python installed on your system, then run the script:</p>
    
  <h2>Code Overview</h2>
    <ul>
        <li><strong>roll():</strong> A function that simulates rolling a six-sided die.</li>
        <li><strong>Player Input:</strong> The game asks for the number of players (2-4).</li>
        <li><strong>Game Loop:</strong> Players take turns rolling the die and accumulating points.</li>
        <li><strong>Winning Condition:</strong> The first player to reach 50 points wins.</li>
    </ul>
        <h2>Example Gameplay</h2>
    <pre>
Enter the number of players(2-4): 3
The number of players is: 3
      
Player 1, Your turn.
      Would you like to roll the dice? (y or n): y
        You rolled a 5
        Your score is: 5
      Would you like to roll the dice? (y or n): n

Player 2, Your turn.
      Would you like to roll the dice? (y or n): y
        Oh no! You rolled a 1!
        No points for you, your turn is now over.
    </pre>
    
  <h2>License</h2>
    <p>This project is for educational purposes and is free to use.</p>
