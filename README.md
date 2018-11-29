<h1>myResume</h1>
<h2>Project pre-installing:</h2>
<ul>
  <li>
    <h3>Install Atom</h3>
    <ul>
      <li>use: https://atom.io/</li>
    </ul>
  </li>
  <li>
    <h3>Atom packages</h3>
    <ul>
      <li>Atom-beautify - use Ctrl+Alt+B</li>
      <li>Platformio-ide-terminal - this will install a terminal under shortcut Ctrl + `</li>
      <li>Atom-django</li>
      <li>Autocomplete-python</li>
      <li>Django-templates</li>
    </ul>
  </li>
  <li>
    <h3>Register to GitHub</h3>
    <ul>
      <li>use: https://github.com/</li>
    </ul>
  </li>
</ul>


<h2>Course 1</h2>
<ul>
  <li>
    <h3>Check versions and packages</h3>
    <ul>
      <li>Atom packages</li>
      <li>Python version</li>
    </ul>
  </li>
  <li>
    <h3>Let's build a project!</h3>
    <ul>
      <li>
        <h4>Create a new virtual environment</h4>
        <p>Allow you to have a specific version of the packages: Python, Django, other API’s</p>
        <ol>
          <li>Open a terminal in Atom</li>
          <li>Move to your .venvs folder</li>
          <li>Create the new venv</li>
          <p>virtualenv myResume</p>
          <li>Activate the new venv</li>
          <p>source .../myResume/bin/activate</p>
          <p>pip freeze</p>
          <li>Install Django 2.1.3</li>
          <p>pip install django</p>
          <p>pip freeze</p>
        </ol>
      </li>
      <li>
        <h4>Start a new project</h4>
        <ol>
          <li>Move to projects folder</li>
          <li>Start the new project</li>
          <p>django-admin startproject myResume</p>
        </ol>
      </li>
      <li>
        <h4>Project folders structure</h4>
        <ul>
          <li>myResume</li>
          <ul>
            <li>myResume</li>
            <ul>
              <li>__init__.py</li>
              <p>This is a blank Python script that due to its special name let’s Python know that this directory can be treated as a package</p>
              <li>settings.py</li>
              <p>This is where you will store all your project settings</p>
              <li>urls.py</li>
              <p>This is a Python script that will store all the URL patterns for your project. Basically the different pages of your web application and how to connect to the end user. It use regular expressions.</p>
              <li>wsgi.py</li>
              <p>This is a Python script that acts as the Web Server Gateway Interface. It will later on help us deploy our web app to production.</p>
            </ul>
            <li>manage.py</li>
            <p>This is a Python script that will use a lot. It will be associates with many commands as we build our web app.
              Will execute parts of django from your project.
            </p>
          </ul>
        </ul>
      </li>
      <li>
        <h4>Run a Django server</h4>
        <ol>
          <li>Move to myResume folder</li>
          <li>Start server</li>
          <p>python manage.py runserver</p>
          <li>Copy to your browser and run http://127.0.0.1:8000/</li>
          <li>Migrate your database</li>
        </ol>
      </li>
      <li>
        <h4>Setup project to use local_settings</h4>
        <ol>
          <li>local_settings.py</li>
              from .settings import *
              DEBUG = True
              ALLOWED_HOSTS = ['*']
          <li>manage.py</li>
              os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume.local_settings")
        </ol>
      </li>
      <li>
        <h4>Save your venvs packages versions in a requirements.tx</h4>
        <ul>
          <li>To save the packages:</li>
          pip freeze > requirements.txt
          <li>To install the packages:</li>
          pip install -r requirements.txt
        </ul>
      </li>
    </ul>
  </li>
  <li>
    <h3>GitHub - first repository</h3>
    <ul>
      <li>Go to https://github.com/ and create a new repository myResume</li>
      <li>Install git</li>
      <li>Create a .gitignore</li>
      <li>Git configuration</li>
      <ul>
        <li>git config --global user.name "#git_user_name"</li>
        <li>git config --global user.email "#git_email"</li>
        <li>git init</li>
        <li>git remote add origin git@gitlab.com:#git_user_name/myResume.git</li>
        <li>README.md</li>
        <li>git add .</li>
        <li>git commit -m "Initial commit"</li>
        <li>git push -u origin master</li>
      </ul>
    </ul>
  </li>
</ul>
<h2>Course 2</h2>
