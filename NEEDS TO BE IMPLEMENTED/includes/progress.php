<div id="leftsidebar">
    <div class="progressdiv sidebardiv leftdiv" style="z-index: -2">
        <?php
        try {
            $num = 0;
            $stmt = $db->prepare('SELECT title, done, episodes FROM projects WHERE status = "i" ORDER BY title');
            $stmt->execute();
            while ($row = $stmt->fetch()) {
                echo '<p style="font-weight: 700; margin-bottom: 0.5em">' . $row['title'] . '</p>';
                $percentage = round($row['done'] * (1 / $row['episodes']) * 100);
                echo '<div><div class="progressbar_outline" style="line-height: 170%; position: relative; margin-bottom: 2em; text-align: center; border-radius: 15px">Folge ' . $row['done'] . ' von ' . $row['episodes'] .
                    '<div class="progressbar"style="border-radius: 15px;position: absolute;top: 0px;left: 0px;height: 100%;width: ' . $percentage . '%; z-index: -1;"></div></div></div>';
                if ($row['episodes'] > 0)
                    $num++;
            }
            if ($num == 0) {
                echo '<p>Derzeit gibt es keine laufenden Projekte</p>';
            }

        } catch (PDOException $e) {
            echo $e->getMessage();      /* lel, error handling EleGiggle */
        }
        ?>
    </div>
</div>