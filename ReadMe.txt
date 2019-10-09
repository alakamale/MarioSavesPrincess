{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mario Saving Princess\n",
    "Finding the all shortest path possible from Mario to Princess."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Requirements\n",
    "- flask\n",
    "- jsonify\n",
    "- flask_sqlalchemy \n",
    "- datetime\n",
    "- werkzeug"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# How to Execute "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-1-15fa48bd973a>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-1-15fa48bd973a>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    python run.py\u001b[0m\n\u001b[1;37m             ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "python run.py"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task List\n",
    "- First task : Mario saving the princess\n",
    "- Second task : API and Database\n",
    "- Third task : Interactive App"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Results"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Endpoint 1\n",
    "Solution to first task\n",
    "- #### /mario/<<int:glen>>/< grid>\n",
    "\n",
    "The ***glen*** refers to the size of the grid, and the ***grid*** is a string of comma separate rows. <br/>\n",
    "</br>\n",
    "e.g.\n",
    " * /mario/3/--m,-x-,-p-"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " ```json\n",
    "[\n",
    "  [\n",
    "    \"DOWN\",  \n",
    "    \"DOWN\", \n",
    "    \"RIGHT\"\n",
    "  ]\n",
    "]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " * /mario/4/--m-,-xx-,--p-,-x--"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "```json\n",
    "[\n",
    "  [\n",
    "    \"RIGHT\", \n",
    "    \"DOWN\", \n",
    "    \"DOWN\", \n",
    "    \"LEFT\"\n",
    "  ]\n",
    "]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Endpoint 2\n",
    "Viewpoint for all logs in the database\n",
    "- #### /log\n",
    "\n",
    "This will return a json object of all the rows in the api database\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "```json\n",
    "[\n",
    "    [\n",
    "    \"grid_map\": \"['---m', '---p', '----', '-x--']\", \n",
    "    \"grid_size\": \"4\", \n",
    "    \"short_path(s)\": \"[('DOWN',)]\", \n",
    "    \"time_log\": \"Tue, 08 Oct 2019 20:59:57 GMT\"\n",
    "  ], \n",
    "  [\n",
    "    \"grid_map\": \"['---m', '---x', '----', '-x-p']\", \n",
    "    \"grid_size\": \"4\", \n",
    "    \"short_path(s)\": \"[('LEFT', 'DOWN', 'DOWN', 'DOWN', 'RIGHT'), ('LEFT', 'DOWN', 'DOWN', 'RIGHT', 'DOWN')]\", \n",
    "    \"time_log\": \"Tue, 08 Oct 2019 21:00:12 GMT\"\n",
    "  ], \n",
    "  [\n",
    "    \"grid_map\": \"['--m', '-x-', '--p']\", \n",
    "    \"grid_size\": \"3\", \n",
    "    \"short_path(s)\": \"[('DOWN', 'DOWN')]\", \n",
    "    \"time_log\": \"Tue, 08 Oct 2019 21:03:43 GMT\"\n",
    "  ]\n",
    "]\n",
    "``` "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Endpoint 3\n",
    "I tried using some HTML+JS+CSS to make it little interactive.\n",
    "- #### /"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here\n",
    "1. Enter the grid size int the text box.\n",
    "2. Click on \"Click here for Grid Details\" "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"11.png\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. After filling, hit submit."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"22.png\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. It will take you to gui solution page."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"3.png\">"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
