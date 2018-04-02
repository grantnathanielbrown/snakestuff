# Grant's Python Experiment
### Why did you choose this subject?

I learned some Python syntax about 2 years ago, so I already had some building blocks for the language. Also, Zakk mentioned Python is popular in D.C., so I figured it would look good on my resume if I developed even a small Python app. My brother also loves Python.

### What problem does it solve?

Python doesn't solve any one "problem", but here are some ways in which avoids problems that other languages have.

1. Python is an "interpreted" language, meaning you don't have to use a compiler to run it (just like JavaScript!). Also, you can interact with the interpreter in real time (kind of like the terminal) to test stuff out.
2. Python is a "high level" language, so it abstracts a lot of stuff, and has variables types similar to JavaScript, which is covenient.
3. Python isn't statically typed, so you don't have to declare variables before using them. (although sometimes people want languages to be statically typed to avoid errors)
4. The syntax is Python is simple compared to other languages; this article (https://www.codeschool.com/blog/2016/01/27/why-python/) gives a good example. 

(Java)
public class Main {
  public static void main(String[] args) {
     System.out.println("hello world");
   }
}

(Python)
print(‘hello world’)

You can also set Python up pretty quickly.

### Why does one use it?

Someone might use it for a lot of the reasons that I just stated above. In general, Python is simpler, and it's a lot easier for people to learn if they are beginner / intermediate coders. It also happens to be one of the most popular languages; GitHub lists Python as the 3rd most popular language used across its repositories. Python has also been getting regular updates for a while.

Python is such a broad language that there are lots of alternatives: there are Java, JavaScript, C++, and more. You could use Java or C++ if you wanted explicit typing, for example.

### What is the history of this technology?

Python was created by Guido van Rossum in 1991. The idea behind Python is to have a language that doesn't require lots of complicated syntax, that also looks pretty. For example, there is a bit of clever functionality with whitespace indicating breaks in the code, as opposed to curly braces.

### What is your opinion on the technology after having built something with it?

I like Python so far; it's pretty easy to learn, especially after seeing JavaScript. It gives the coder a lot of freedom with the dynamic typing. It could be kind of annoying to scale out, though, because of the way that programs run in sequential order. Also, this makes testing difficult (which is why I need to learn unit testing!)

### What are the biggest conceptual hurdles (if any) you encountered when researching this?

It took me about 15 minutes to actualize how Python really worked; I didn't realize that it was an "interpreted" language, so I thought it needed a compiler to run. I finally got that you could just run it in the terminal, after installing it on your computer. The way that variable scoping works in Python is also different; to access global variables, you can just reference them, but in order to change their values, you need to include the keyword "global" when you reference it inside of a function, or whatever.

### What article or forum was most helpful to you in learning this?

My attention span is short, so I used lots of random articles and, of course, stack overflow. The python tutorial in the documentation(https://docs.python.org/3/tutorial/index.html) was good for starting out. Also, this article explains which version of Python you should use (http://docs.python-guide.org/en/latest/starting/which-python/).

Finally, these tiny example programs helped me understand things. https://wiki.python.org/moin/SimplePrograms

To run my little project, just clone this repo, CD into the folder, and type python ./experiment.py




