package com.example.nerdherd;

import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.method.HideReturnsTransformationMethod;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class SignupActivity extends AppCompatActivity {

    Button confirm_signup_btn;
    EditText email_field;
    EditText password_field;
    EditText confirm_password_field;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);

        //initializing the layout widgets
        confirm_signup_btn = findViewById(R.id.signup_confirm_btn);
        email_field = findViewById(R.id.email);
        password_field = findViewById(R.id.password);
        confirm_password_field = findViewById(R.id.confirm_password);

        //setting intents for signup btn
        confirm_signup_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = SignupActivity.this;
                //go to main page if every field is valid
                if(validityCheck()){
                    Class mainPageActivity = MainPageActivity.class;
                    Intent intent = new Intent(context, mainPageActivity);
                    startActivity(intent);
                } else {
                    //TODO if not every field valid then highlight the problem and remain on signup page
                        //TODO cont. maybe a TOAST msg or something similar
                }


            }
        });

        //hiding password fields
        password_field.setTransformationMethod(HideReturnsTransformationMethod.getInstance());
        confirm_password_field.setTransformationMethod(HideReturnsTransformationMethod.getInstance());
    }

    public static boolean validityCheck(){
        return true;
    }
}
