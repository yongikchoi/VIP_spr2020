import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

// PURPOSE
// Given a photo ID range produce a txt file to upload into CloudCompare of a smaller LiDAR data section

// INSTRUCTIONS
// 1. Make sure your year's _coords.csv and LiDAR txt file are placed in the same folder as this script
// 2. Open terminal and change to the directory holding this script
// 3. Compile: javac Section.java
// 4. Run: java Section <start_pic_number>  <end_pic_number> <year> <LiDAR_filename.txt>
// Done. Produced txt file <year>_LiDAR_Section.txt which is a select range of LiDAR data points

public class Section {

    public static void main(String args[]) {
      //Retrieve terminal arguments
      int start_pic = Integer.valueOf(args[0]); //ex: 1650
      int end_pic = Integer.valueOf(args[1]); //ex: 2880
      String year = args[2]; //ex: 2018
      String lidarTXT = args[3]; //ex: V_20180816_I285_EB_run1.txt
      //*Can't have parenthesis in file name


      getSection(start_pic, end_pic, year, lidarTXT);
    }

    public static void getSection(int start_pic, int end_pic, String year, String lidarTXT) {
        String startPicRow;
        String endPicRow;
        String currRow;

        double startEasting = 0; //dummy initialization
        double startNorthing = 0;
        double endEasting = 0;
        double endNorthing = 0;

        try {


            System.out.println("Part 1/3: Finding start and end pic data from " + year + "_coords.csv");
            //Get data of start and end pics
            BufferedReader csvReader = new BufferedReader(new FileReader(year + "_coords.csv"));
            csvReader.readLine();

            while ((currRow = csvReader.readLine()) != null) {
                String[] data = currRow.split(",");

                String picID = data[0];

                if (Integer.valueOf(picID) == start_pic) {
                    startPicRow = currRow;
                    startEasting = Double.valueOf(data[1]);
                    startNorthing = Double.valueOf(data[2]);
                }

                if (Integer.valueOf(picID) == end_pic) {
                    endPicRow = currRow;
                    endEasting = Double.valueOf(data[1]);
                    endNorthing = Double.valueOf(data[2]);
                    break;
                }
            }

            try {
                csvReader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }


            System.out.println("Part 2/3: Finding closest LiDAR points to both start and end pic UTM coordinates...");
            //Find LiDAR data points closest to start and end pic UTM coords
            BufferedReader txtReader = new BufferedReader(new FileReader(lidarTXT));
            txtReader.readLine();

            double currEasting;
            double currNorthing;
            double minStartDistance = Double.MAX_VALUE;
            double minEndDistance = Double.MAX_VALUE;
            double currStartDistance;
            double currEndDistance;
            String startLidarID = "-1"; //dummy initialization
            String endLidarID = "-1";

            while ((currRow = txtReader.readLine()) != null) {
                String[] data = currRow.split(" ");

                currEasting = Double.valueOf(data[1]);
                currNorthing = Double.valueOf(data[2]);

                currStartDistance = getDistance(currEasting, startEasting, currNorthing, startNorthing);
                if (currStartDistance < minStartDistance) {
                    minStartDistance = currStartDistance;
                    startLidarID = data[0];
                }

                currEndDistance = getDistance(currEasting, endEasting, currNorthing, endNorthing);
                if (currEndDistance < minEndDistance) {
                    minEndDistance = currEndDistance;
                    endLidarID = data[0];
                }
            }

            try {
                txtReader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }



            System.out.println("Part 3/3: Writing to new txt file the LiDAR points in point range found in Part 2...");
            //Write to a new txt file, the LiDAR points between the two LiDAR points foudn in previous section
            FileWriter csvWriter = new FileWriter(year + "_LiDAR_Section.txt");

            BufferedReader txtReader2 = new BufferedReader(new FileReader(lidarTXT));
            currRow = txtReader2.readLine();
            csvWriter.append(currRow);
            csvWriter.append("\n");

            int idCount = 0;

            while (idCount != Integer.valueOf(startLidarID)) {
                txtReader2.readLine();
                idCount++;
            }

            while (idCount != Integer.valueOf(endLidarID) + 1) {
                currRow = txtReader2.readLine();
                csvWriter.append(currRow);
                csvWriter.append("\n");
                idCount++;
            }

            try {
                txtReader2.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            csvWriter.flush();
            csvWriter.close();


        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Done! See produced txt file " + year + "_LiDAR_Section.txt");
    }

    //Calculation for distance between two UTM coordinates.
    public static double getDistance(double eastingOne, double eastingTwo, double northingOne, double northingTwo) {
        return Math.sqrt(Math.pow((eastingOne - eastingTwo), 2) + Math.pow((northingOne - northingTwo),2));
    }
}


