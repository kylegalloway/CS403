function createEnv() {
  // empty environment
  return cons(ENV, null,
            cons(JOIN, null, null));
}
// env = environment inserting into
function insert(identifier, value, env) {
  var ids = car(env);
  var vals = cadr(env);
  env.left = cons(JOIN, id, ids);
  env.right.left=cons(JOIN,val,vals);
}

function lookup(id,env) {
  var ids = car(env);
  var vals = cadr(env);
}
