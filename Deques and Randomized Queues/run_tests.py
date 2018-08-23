import datetime, os, signal, subprocess, sys, time, unittest

def run(command, stdin = None, timeout = 30):
    """
    Runs the specified command using specified standard input (if any) and
    returns the output on success. If the command doesn't return within the
    specified time (in seconds), "__TIMEOUT__" is returned.
    """

    start = datetime.datetime.now()
    process = subprocess.Popen(command.split(),
                               stdin = subprocess.PIPE, 
                               stdout = subprocess.PIPE,
                               stderr = subprocess.STDOUT)
    if not stdin is None:
        process.stdin.write(bytes(stdin, 'utf-8'))
    process.stdin.close()
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return "__TIMEOUT__"
    result = process.stdout.read().decode("utf-8")
    process.stdout.close()
    return result

class Problem1(unittest.TestCase):
    
    def test1(self):
        command = "java LinkedDeque"
        sought = """false
(364 characters) There is grandeur in this view of life, with its several powers, having been originally breathed into a few forms or into one; and that, whilst this planet has gone cycling on according to the fixed law of gravity, from so simple a beginning endless forms most beautiful and most wonderful have been, and are being, evolved. ~ Charles Darwin, The Origin of Species
true
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem2(unittest.TestCase):
    
    def test1(self):
        command = "java ResizingArrayRandomQueue"
        sought = """55
0
55
true
"""
        got = run(command, " ".join([str(i) for i in range(11)]))
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem3(unittest.TestCase):
    
    def test1(self):
        command = "java Subset 3"
        got = run(command, "A B C D E F G H I")
        self.assertNotEqual(got, "__TIMEOUT__")
        a, b = got.split(), "A B C D E F G H I".split()
        self.assertTrue(len(a) == 3 and set(a).issubset(set(b)))

    def test2(self):
        command = "java Subset 3"
        got = run(command, "A B C D E F G H I")
        self.assertNotEqual(got, "__TIMEOUT__")
        a, b = got.split(), "A B C D E F G H I".split()
        self.assertTrue(len(a) == 3 and set(a).issubset(set(b)))

    def test3(self):
        command = "java Subset 8"
        got = run(command, "AA BB BB BB BB BB CC CC")
        self.assertNotEqual(got, "__TIMEOUT__")
        a, b = got.split(), "AA BB BB BB BB BB CC CC".split()
        self.assertTrue(set(a) == set(b))
        
if __name__ == "__main__":
    unittest.main()
