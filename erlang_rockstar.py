from rockstar import RockStar

erlang_code = 'io:format("~s~n", ["Hello, world!"])'
rock_it_bro = RockStar(days=450, file_name='helloworld.erl', code=erlang_code)
rock_it_bro.make_me_a_rockstar()
