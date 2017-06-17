class Animate:
    pass
class Inanimate:
    pass
class Animals(Animate):
      def eat_leaves(self):
        print('eating')
class Mammals(Animals):
    pass
class Giraffes(Mammals):
  
    def feed_milk(self):
        print('feeding')
class Sidewalks(Inanimate):
    pass

renold=Giraffes() ## renold is the object of Giraffes class
harold=Giraffes()

renold.eat_leaves()
harold.feed_milk ()

    
    
