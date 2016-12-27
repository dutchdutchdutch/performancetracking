from .views import app
from .modo import graph

graph.data("CREATE CONSTRAINT ON (n:User) ASSERT n.username IS UNIQUE")
graph.data("CREATE CONSTRAINT ON (n:Post) ASSERT n.id IS UNIQUE")
graph.data("CREATE CONSTRAINT ON (n:Tag) ASSERT n.name IS UNIQUE")
graph.data("CREATE INDEX ON :Post(date)")