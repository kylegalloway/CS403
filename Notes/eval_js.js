function extendEnv(vars, vals, env) {
	return cons(ENV, vars, cons(JOIN, vals, cons(JOIN, env, null)));
}

function createEnv() {
	extendEnv(null, null, null);
}

function lookup(id, env) {
	while (env != null) {
		var ids = car(env);
		var vals = cadr(env);
		var outer = caddr(env);

		while (ids != null) {
			// ...
		}

		env = caddr(outer);
	}
}
// // like lookup, but set instead of gets
// function updateEnv(???) {
//     // ...
// }

function assign(t, e) {
	updateEnv(t.left, eval(t.right, e));
}

function eval(t, e) {
	if (t.type == INTEGER) {
		return t;
	} else if (t.type == STRING) {
		return t;
	} else if (t.type == ID) {
		return lookup(t, e);
	} else if (t.type == ASSIGN) {
		return assign(t, e);
	}
}

function main(argc, argv) {
	lexInit(argv);
	var pt = parse();
	var env = createEnv();
	eval(pt, env);
}
