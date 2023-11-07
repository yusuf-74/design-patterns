"""
Module: Bridge Pattern Implementation

Description:
Welcome to the "Bridge Pattern Implementation" module. 
This module explores and demonstrates the Bridge design pattern, a structural pattern in software design. 
The Bridge pattern is used to separate an object's abstraction from its implementation, allowing both to vary independently.

Module Overview:
- Problem Description: 
    We will begin by presenting a scenario where you have abstractions and multiple implementations. 
    Managing these abstractions and their various implementations can become complex and tightly coupled, 
    leading to maintenance challenges.

- Solving with Bridge Pattern: 
    Next, we will implement the Bridge pattern to address the problem of tightly coupled abstractions and implementations. 
    The Bridge Pattern decouples these aspects, promoting flexibility, extensibility, and easier maintenance by separating concerns.

- Real-world Example: 
    To illustrate the advantages of the Bridge Pattern, we'll provide a practical example that demonstrates 
    how it simplifies complex software systems and supports independent changes.

Client Code:
- The client code will showcase the usage of the Bridge Pattern. It will create an abstraction and assign different implementations to it, showing how the pattern facilitates decoupling and flexibility.
"""

# Bridge Pattern Example: View-Resources

from abc import ABC, abstractmethod

# Implementor Interface: Resource

class Resource(ABC):
    @abstractmethod
    def get_snippet(self):
        pass
    
    @abstractmethod
    def get_title(self):
        pass
    
    @abstractmethod
    def get_image(self):
        pass
    
    @abstractmethod
    def get_url(self):
        pass


# Concrete Implementors: Albums, Artists, and Songs
class Albums(Resource):
    def get_snippet(self):
        return "Album snippet"

    def get_title(self):
        return "Album title"

    def get_image(self):
        return "Album image"

    def get_url(self):
        return "Album URL"

class Artists(Resource):
    def get_snippet(self):
        return "Artist snippet"

    def get_title(self):
        return "Artist title"

    def get_image(self):
        return "Artist image"

    def get_url(self):
        return "Artist URL"

class Songs(Resource):
    def get_snippet(self):
        return "Song snippet"

    def get_title(self):
        return "Song title"

    def get_image(self):
        return "Song image"

    def get_url(self):
        return "Song URL"

# Abstraction Interface: View

class View(ABC):
    def __init__(self, resource):
        self.resource : Resource = resource
    @abstractmethod
    def show(self):
        pass

# Refined Abstraction: LongFormView
class LongFormView(View):
    def show(self):
        snippet = self.resource.get_snippet()
        title = self.resource.get_title()
        image = self.resource.get_image()
        url = self.resource.get_url()
        return f"Long Form View:\nTitle: {title}\nSnippet: {snippet}\nImage: {image}\nURL: {url}"

# Refined Abstraction: PopupView
class PopupView(View):
    def show(self):
        snippet = self.resource.get_snippet()
        title = self.resource.get_title()
        image = self.resource.get_image()
        url = self.resource.get_url()
        return f"Popup View:\nTitle: {title}\nSnippet: {snippet}\nImage: {image}\nURL: {url}"

# Refined Abstraction: ShortFormView
class ShortFormView(View):
    def show(self):
        snippet = self.resource.get_snippet()
        title = self.resource.get_title()
        image = self.resource.get_image()
        url = self.resource.get_url()
        return f"Short Form View:\nTitle: {title}\nSnippet: {snippet}\nImage: {image}\nURL: {url}"

# Client Code
if __name__ == "__main__":
    albums = Albums()
    artists = Artists()
    songs = Songs()

    long_albums_view = LongFormView(albums)
    popup_artists_view = PopupView(artists)
    short_songs_view = ShortFormView(songs)

    print(long_albums_view.show())
    print(popup_artists_view.show())
    print(short_songs_view.show())
